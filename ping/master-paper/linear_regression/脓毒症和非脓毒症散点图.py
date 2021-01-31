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
df = pd.read_csv("../data-final.csv")
print(df.columns)
plt.figure(figsize=(10, 4))

# 脓毒症组合非脓毒症组
# -------(1)脓毒症组：百分比与血乳酸-------------
ax1 = plt.subplot(1, 2, 1)
df1 = df[["脓毒症组单核细胞PD-L1", "脓毒症组血乳酸mmol/L"]]
df1 = df1.dropna()
X = df1["脓毒症组单核细胞PD-L1"].values.reshape(-1, 1)
y = df1["脓毒症组血乳酸mmol/L"].values.reshape(-1, 1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("单核细胞PD-L1百分比（%）", fontsize=20)
plt.ylabel("血乳酸mmol/L", fontsize=20)

model = linear_model.LinearRegression()
model.fit(X, y)
print(model.coef_)
print(model.intercept_)
print(model.score(X, y))
ax1.plot(X, y, linestyle='none', marker='o', alpha=0.6)
y2 = model.predict(X)
ax1.plot(X, y2, '-', color='dodgerblue')
ax1.text(x=60, y=16, s='$^{*}r=0.575$', fontsize=20)
ax1.text(x=60, y=13, s='$p=0.000$', fontsize=20)
ax1.set_title("(a)脓毒症组", y=-0.4, fontsize=20)
set_ax(ax1)

# -------(2)脓毒症组：百分比与PCT-------------
ax2 = plt.subplot(1, 2, 2)
df2 = df[["脓毒症组单核细胞PD-L1", "脓毒症组PCT"]]
df2 = df2.dropna()
X = df2["脓毒症组单核细胞PD-L1"].values.reshape(-1, 1)
y = df2["脓毒症组PCT"].values.reshape(-1, 1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("单核细胞PD-L1", fontsize=20)
plt.ylabel("PCT", fontsize=20)

model = linear_model.LinearRegression()
model.fit(X, y)
print(model.coef_)
print(model.intercept_)
print(model.score(X, y))
ax2.plot(X, y, linestyle='none', marker='D', color="orange", alpha=0.6)
y2 = model.predict(X)
ax2.plot(X, y2, '-', color='dodgerblue')
ax2.text(x=60, y=160, s='$^{*}r=0.549$', fontsize=20)
ax2.text(x=60, y=130, s='$p=0.000$', fontsize=20)
ax2.set_title("(b)脓毒症组", y=-0.4, fontsize=20)
set_ax(ax2)

# # -------(3)非脓毒症组：百分比与血乳酸-------------
# ax3 = plt.subplot(2, 2, 3)
# df3 = df[["脓毒症组单核细胞PD-L1百分比（%）对照组", "脓毒症组血乳酸mmol/L对照组"]]
# df3 = df3.dropna()
# X = df3["脓毒症组单核细胞PD-L1百分比（%）对照组"].values.reshape(-1, 1)
# y = df3["脓毒症组血乳酸mmol/L对照组"].values.reshape(-1, 1)
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.xlabel("", fontsize=20)
# plt.ylabel("", fontsize=20)
#
# model = linear_model.LinearRegression()
# model.fit(X, y)
# print(model.coef_)
# print(model.intercept_)
# print(model.score(X, y))
# ax3.plot(X, y, 'k.')
# y2 = model.predict(X)
# ax3.plot(X, y2, '-', color='dodgerblue')
# ax3.text(x=1.2, y=350, s='$y=145.2560x-36.7859$')
# ax3.text(x=1.2, y=320, s='$R^2=0.9758$')
# ax3.set_title("(a)", y=-0.2, fontsize=20)
# set_ax(ax3)
#
# # -------(4)非脓毒症组：百分比与PCT-------------
# ax4 = plt.subplot(2, 2, 4)
# df4 = df[["脓毒症组单核细胞PD-L1百分比（%）对照组", "脓毒症组PCT对照组"]]
# df4 = df4.dropna()
# X = df4["脓毒症组单核细胞PD-L1百分比（%）对照组"].values.reshape(-1, 1)
# y = df4["脓毒症组PCT对照组"].values.reshape(-1, 1)
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.xlabel("", fontsize=20)
# plt.ylabel("", fontsize=20)
#
# model = linear_model.LinearRegression()
# model.fit(X, y)
# print(model.coef_)
# print(model.intercept_)
# print(model.score(X, y))
# ax4.plot(X, y, 'k.')
# y2 = model.predict(X)
# ax4.plot(X, y2, '-', color='dodgerblue')
# ax4.text(x=1.2, y=350, s='$y=145.2560x-36.7859$')
# ax4.text(x=1.2, y=320, s='$R^2=0.9758$')
# ax4.set_title("(a)", y=-0.2, fontsize=20)
# set_ax(ax4)
plt.show()