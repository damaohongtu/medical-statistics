from __future__ import print_function
import os
import sys
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.layers import Dense, Input, GlobalMaxPooling1D
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.models import Model
from keras.initializers import Constant
from keras.callbacks import ModelCheckpoint

BASE_DIR = ''
# glove模型路径
GLOVE_DIR = os.path.join(BASE_DIR, 'glove.6B')
# 文本语料路径
TEXT_DATA_DIR = os.path.join(BASE_DIR, '20_newsgroup')
MAX_SEQUENCE_LENGTH = 1000
MAX_NUM_WORDS = 20000
EMBEDDING_DIM = 100
VALIDATION_SPLIT = 0.2

# first, build index mapping words in the embeddings set
# to their embedding vector
# 1.准备glove词向量和它们对应的字典映射

print('Indexing word vectors.')
# 我们从GloVe文件中解析出每个词和它所对应的词向量，并用字典的方式存储
embeddings_index = {}
with open(os.path.join(GLOVE_DIR, 'glove.6B.100d.txt')) as f:
    for line in f:
        word, coefs = line.split(maxsplit=1)
        coefs = np.fromstring(coefs, 'f', sep=' ')
        embeddings_index[word] = coefs

print('Found %s word vectors.' % len(embeddings_index))

# second, prepare text samples and their labels
print('Processing text dataset')

# 我们首先遍历下语料文件下的所有文件夹，获得不同类别的新闻以及对应的类别标签，代码如下所示
texts = []  # list of text samples
labels_index = {}  # dictionary mapping label name to numeric id
labels = []  # list of label ids
for name in sorted(os.listdir(TEXT_DATA_DIR)):
    path = os.path.join(TEXT_DATA_DIR, name)
    if os.path.isdir(path):
        label_id = len(labels_index)
        labels_index[name] = label_id
        for fname in sorted(os.listdir(path)):
            if fname.isdigit():
                fpath = os.path.join(path, fname)
                args = {} if sys.version_info < (3,) else {'encoding': 'latin-1'}
                with open(fpath, **args) as f:
                    t = f.read()
                    i = t.find('\n\n')  # skip header
                    if 0 < i:
                        t = t[i:]
                    texts.append(t)
                labels.append(label_id)
# print(texts[0],labels[0])
print('Found %s texts.' % len(texts))
# 之后，我们可以新闻样本转化为神经网络训练所用的张量。所用到的Keras库是keras.preprocessing.text.Tokenizer和keras.preprocessing.sequence.pad_sequences。代码如下所示
# finally, vectorize the text samples into a 2D integer tensor
# tokenizer计算机在处理语言文字时，是无法理解文字的含义，通常会把一个词（中文单个字或者词组认为是一个词）转化为一个正整数，于是一个文本就变成了一个序列。而tokenizer的核心任务就是做这个事情。
# 具体参考：https://www.jianshu.com/p/ac721387fe48
tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))
# 为了实现的简便，keras只能接受长度相同的序列输入。因此如果目前序列长度参差不齐，这时需要使用pad_sequences()。该函数是将序列转化为经过填充以后的一个长度相同的新序列新序列。
data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
print(data)
# data变成文本个数*MAX_SEQUENCE_LENGTH的形状
# to_categorical就是将类别向量转换为二进制（只有0和1）的矩阵类型表示。其表现为将原有的类别向量转换为独热编码的形式
labels = to_categorical(np.asarray(labels))
print(labels)
# labels变成文本个数*分类个数的形状
print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', labels.shape)

# split the data into a training set and a validation set
indices = np.arange(data.shape[0])
# print(indices)
# np.random.shuffle(x) 现场修改序列，改变自身内容。（类似洗牌，打乱顺序）
np.random.shuffle(indices)
data = data[indices]
print(data)
labels = labels[indices]
print(labels)
num_validation_samples = int(VALIDATION_SPLIT * data.shape[0])
print(data.shape[0])
x_train = data[:-num_validation_samples]
y_train = labels[:-num_validation_samples]
x_val = data[-num_validation_samples:]
y_val = labels[-num_validation_samples:]

print('Preparing embedding matrix.')

# prepare embedding matrix
num_words = min(MAX_NUM_WORDS, len(word_index) + 1)
# 此时，我们可以根据得到的字典生成上文所定义的词向量矩阵
embedding_matrix = np.zeros((num_words, EMBEDDING_DIM))
for word, i in word_index.items():
    if i >= MAX_NUM_WORDS:
        continue
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        # words not found in embedding index will be all-zeros.
        # 从预训练模型的词向量到语料库的词向量映射
        embedding_matrix[i] = embedding_vector

# load pre-trained word embeddings into an Embedding layer
# note that we set trainable = False so as to keep the embeddings fixed
# 现在我们将这个词向量矩阵加载到Embedding层中，注意，我们设置trainable=False使得这个编码层不可再训练。
embedding_layer = Embedding(num_words,
                            EMBEDDING_DIM,
                            embeddings_initializer=Constant(embedding_matrix),
                            input_length=MAX_SEQUENCE_LENGTH,
                            trainable=False)

print('Training model.')

# train a 1D convnet with global maxpooling
sequence_input = Input(shape=(MAX_SEQUENCE_LENGTH,), dtype='int32')
embedded_sequences = embedding_layer(sequence_input)
x = Conv1D(128, 5, activation='relu')(embedded_sequences)
x = MaxPooling1D(5)(x)
x = Conv1D(128, 5, activation='relu')(x)
x = MaxPooling1D(5)(x)
x = Conv1D(128, 5, activation='relu')(x)
x = GlobalMaxPooling1D()(x)
x = Dense(128, activation='relu')(x)
preds = Dense(len(labels_index), activation='softmax')(x)

model = Model(sequence_input, preds)
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['acc'])
# checkpoint
filepath = "weights-improvement-{epoch:02d}-{val_acc:.2f}.hdf5"
# 中途训练效果提升, 则将文件保存, 每提升一次, 保存一次
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True,
                             mode='max')
callbacks_list = [checkpoint]
model.fit(x_train, y_train,
          batch_size=128,
          epochs=2,
          validation_data=(x_val, y_val))