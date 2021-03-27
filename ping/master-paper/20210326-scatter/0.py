import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
plt.rcParams['font.sans-serif'] = ['SimHei']

def set_ax(ax):
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ###设置右边坐标轴的粗细

color = ['orangered', 'g', 'blue', 'k']
df = pd.read_csv("../20210326-final.csv")
print(df.columns)
plt.figure(figsize=(8, 8))

# 脓毒症组合非脓毒症组
# -------(1)脓毒症组：百分比与血乳酸-------------
ax1 = plt.subplot(1, 1, 1)
df1 = df[['病例组第3天单核细胞PD-L1（%）', '病例组第3天血乳酸mmol/L']]
df1 = df1.dropna()
X = df1["病例组第3天单核细胞PD-L1（%）"].values.reshape(-1, 1)
y = df1["病例组第3天血乳酸mmol/L"].values.reshape(-1, 1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("第3天单核细胞PD-L1(%)", fontsize=20)
plt.ylabel("第3天血乳酸(mmol/L)", fontsize=20)

model = linear_model.LinearRegression()
model.fit(X, y)
print(model.coef_)
print(model.intercept_)
print(model.score(X, y))
ax1.plot(X, y, linestyle='none', marker='o', alpha=0.6)
y2 = model.predict(X)
ax1.plot(X, y2, '-', color='dodgerblue')
ax1.text(x=35, y=4, s='$r=0.415$', fontsize=20)
ax1.text(x=35, y=4.5, s='$p=0.205$', fontsize=20)
# ax1.set_title("(a)脓毒症组", y=-0.4, fontsize=20)
ax1.set_title("病例组", y=-0.2, fontsize=20)

set_ax(ax1)

plt.show()