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
plt.figure(figsize=(10, 8))

# -------(1)脓毒症存活组：百分比与血乳酸-------------
ax1 = plt.subplot(2, 2, 1)
df1 = df[["脓毒症存活组单核细胞PD-L1百分比（%）", "脓毒症存活组血乳酸"]]
df1 = df1.dropna()
X = df1["脓毒症存活组单核细胞PD-L1百分比（%）"].values.reshape(-1, 1)
y = df1["脓毒症存活组血乳酸"].values.reshape(-1, 1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("单核细胞PD-L1百分比（%）", fontsize=20)
plt.ylabel("血乳酸", fontsize=20)

model = linear_model.LinearRegression()
model.fit(X, y)
print(model.coef_)
print(model.intercept_)
print(model.score(X, y))
ax1.plot(X, y, linestyle='none', marker='o', alpha=0.6)
y2 = model.predict(X)
ax1.plot(X, y2, '-', color='dodgerblue')
ax1.text(x=20, y=7, s='$^{*}r=0.587$', fontsize=20)
ax1.text(x=20, y=6, s='$p=0.000$', fontsize=20)
ax1.set_title("(a)存活组", y=-0.35, fontsize=20)
set_ax(ax1)

# -------(2)脓毒症存活组：百分比与PCT-------------
ax2 = plt.subplot(2, 2, 2)
df2 = df[["脓毒症存活组单核细胞PD-L1百分比（%）", "脓毒症存活组PCT"]]
df2 = df2.dropna()
X = df2["脓毒症存活组单核细胞PD-L1百分比（%）"].values.reshape(-1, 1)
y = df2["脓毒症存活组PCT"].values.reshape(-1, 1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("单核细胞PD-L1百分比（%）", fontsize=20)
plt.ylabel("PCT", fontsize=20)

model = linear_model.LinearRegression()
model.fit(X, y)
print(model.coef_)
print(model.intercept_)
print(model.score(X, y))
ax2.plot(X, y, linestyle='none', marker='D', color="orange", alpha=0.6)
y2 = model.predict(X)
ax2.plot(X, y2, '-', color='dodgerblue')
ax2.text(x=20, y=160, s='$^{*}r=0.638$', fontsize=20)
ax2.text(x=20, y=125, s='$p=0.000$', fontsize=20)
ax2.set_title("(b)存活组", y=-0.35, fontsize=20)
set_ax(ax2)

# -------(3)脓毒症死亡组：百分比与血乳酸-------------
ax3 = plt.subplot(2, 2, 3)
df3 = df[["脓毒症死亡组单核细胞PD-L1百分比（%）", "脓毒症死亡组血乳酸"]]
df3 = df3.dropna()
X = df3["脓毒症死亡组单核细胞PD-L1百分比（%）"].values.reshape(-1, 1)
y = df3["脓毒症死亡组血乳酸"].values.reshape(-1, 1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("单核细胞PD-L1百分比（%）", fontsize=20)
plt.ylabel("血乳酸", fontsize=20)

model = linear_model.LinearRegression()
model.fit(X, y)
print(model.coef_)
print(model.intercept_)
print(model.score(X, y))
ax3.plot(X, y, linestyle='none', marker='o', color="green", alpha=0.6)
y2 = model.predict(X)
ax3.plot(X, y2, '-', color='dodgerblue')
ax3.text(x=15, y=17.5, s='$^{*}r=0.395$', fontsize=20)
ax3.text(x=15, y=15, s='$p=0.094$', fontsize=20)
ax3.set_title("(c)死亡组", y=-0.35, fontsize=20)
set_ax(ax3)

# -------(4)脓毒症死亡组：百分比与PCT-------------
ax4 = plt.subplot(2, 2, 4)
df4 = df[["脓毒症死亡组单核细胞PD-L1百分比（%）", "脓毒症死亡组PCT"]]
df4 = df4.dropna()
X = df4["脓毒症死亡组单核细胞PD-L1百分比（%）"].values.reshape(-1, 1)
y = df4["脓毒症死亡组PCT"].values.reshape(-1, 1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("单核细胞PD-L1百分比（%）", fontsize=20)
plt.ylabel("PCT", fontsize=20)

model = linear_model.LinearRegression()
model.fit(X, y)
print(model.coef_)
print(model.intercept_)
print(model.score(X, y))
ax4.plot(X, y, linestyle='none', marker='D', color="grey", alpha=0.6)
y2 = model.predict(X)
ax4.plot(X, y2, '-', color='dodgerblue')
ax4.text(x=10, y=25, s='$^{*}r=0.635$', fontsize=20)
ax4.text(x=10, y=20, s='$p=0.015$', fontsize=20)
ax4.set_title("(d)死亡组", y=-0.35, fontsize=20)
set_ax(ax4)

plt.show()