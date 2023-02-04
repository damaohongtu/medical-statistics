import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

def set_ax(ax):
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ###设置右边坐标轴的粗细

color = ['orangered', 'g', 'blue', 'k']
df = pd.read_csv("../2021-05-04.csv")
print(df.columns)
plt.figure(figsize=(8, 8))
# ---------百分比vs乳酸(实验组)----------------
ax1 = plt.subplot(1, 1, 1)
df1 = df[["对照组PCT", "对照组第3天PCT"]]

ax1.boxplot([df1["对照组PCT"].dropna(), df1["对照组第3天PCT"].dropna()], notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['第1天', '第3天'], fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel("降钙素原(pg/ml)", fontsize=16)
# 绘制比较线
x1, x2 = 1, 2
y, h, col = 4.8, 0.1, 'k'
ax1.set_ylim(0, 5.6)
ax1.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax1.text((x1+x2)*.5, y+h+0.1, "$P=.450$", ha='center', va='bottom', color=col, fontsize=20)
ax1.set_title("对照组", y=-0.2, fontsize=20)
set_ax(ax1)
plt.show()