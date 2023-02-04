import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
# 图3-23 血浆IL-1β浓度比较：（a）病例组与对照组第1天血浆IL-1β浓度比较；（b）脓毒症休克组与脓毒症组第1天血浆IL-1β浓度比较
def set_ax(ax):
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ###设置右边坐标轴的粗细

color = ['orangered', 'g', 'blue', 'k']
df = pd.read_csv("../20210326-final.csv")
# df = df.dropna()
print(df.columns)
plt.figure(figsize=(8, 8))
# ---------百分比vs乳酸(实验组)----------------
ax1 = plt.subplot(1, 1, 1)
df1 = df[['脓毒症休克组IL1β第1天', '脓毒症组IL1β第1天']]
# df1 = df1.dropna()
ax1.boxplot([df1["脓毒症休克组IL1β第1天"].dropna(), df1["脓毒症组IL1β第1天"].dropna()], notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['脓毒症休克组', '脓毒症组'], fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel("IL-1β(pg/ml)", fontsize=16)
# 绘制比较线
x1, x2 = 1, 2
y, h, col = 230, 10, 'k'
ax1.set_ylim(0, 260)
ax1.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax1.text((x1+x2)*.5, y+h+1, "$P=.472$", ha='center', va='bottom', color=col, fontsize=20)
# ax1.set_title("(a)", y=-0.2, fontsize=20)
set_ax(ax1)
plt.show()