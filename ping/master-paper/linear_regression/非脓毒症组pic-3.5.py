import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']

def set_ax(ax):
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ###设置右边坐标轴的粗细

color = ['orangered', 'g', 'blue', 'k']
plt.figure(figsize=(8, 8))
ax1 = plt.subplot(1, 1, 1)
# 脓毒症组合非脓毒症组
# -------(1)脓毒症组：百分比与血乳酸-------------

X = [6.79, 1.21, 5.9, 5.74, 3.39, 8.58, 0.68, 1.48, 8.18, 3.26, 15.83, 1.06]
X = np.asarray(X).reshape(-1, 1)
y = [2.1, 2.1, 1.3, 1.5, 1.1, 1.9, 1.7, 1.3, 1, 1.3, 1.5, 2.2]
y = np.asarray(y).reshape(-1, 1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("单核细胞PD-L1百分比（%）", fontsize=20)
plt.ylabel("血乳酸(mmol/L)", fontsize=20)

model = linear_model.LinearRegression()
model.fit(X, y)
print(model.coef_)
print(model.intercept_)
print(model.score(X, y))
ax1.plot(X, y, linestyle='none', marker='o', alpha=0.6)
y2 = model.predict(X)
ax1.plot(X, y2, '-', color='dodgerblue')
ax1.text(x=10, y=1.8, s='$r=-0.258$', fontsize=20)
ax1.text(x=10, y=2.0, s='$p=0.418$', fontsize=20)
ax1.set_title("对照组", y=-0.2, fontsize=20)
set_ax(ax1)

plt.show()