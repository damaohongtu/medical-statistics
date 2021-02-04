#coding=utf-8
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from keras.utils import to_categorical

text = """我是一条天狗呀！
我把月来吞了，
我把日来吞了，
我把一切的星球来吞了，
我把全宇宙来吞了。
我便是我了！"""
sentences = text.split()
sent_words = [list(jieba.cut(sent0)) for sent0 in sentences]
document = [" ".join(sent0) for sent0 in sent_words]
tfidf_model = TfidfVectorizer().fit(document)
sparse_result = tfidf_model.transform(document)     # 得到tf-idf矩阵，稀疏矩阵表示法

print(sparse_result)

print(sparse_result.todense())                     # 转化为更直观的一般矩阵

print(tfidf_model.vocabulary_)                      # 词语与列的对应关系

tfidf_model6 = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b", max_features=10, ngram_range=(1,2), stop_words=["是", "的"]).fit(document)
print(tfidf_model6.vocabulary_)


tfidf_model5 = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b", ngram_range=(1,2), stop_words=["是", "的"]).fit(document)
print(tfidf_model5.get_feature_names())

tfidf_model4 = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b", max_df=0.6, stop_words=["是", "的"]).fit(document)
print(tfidf_model4.vocabulary_)

print(to_categorical([1,2,3,54,6,3,2], num_classes=5))

