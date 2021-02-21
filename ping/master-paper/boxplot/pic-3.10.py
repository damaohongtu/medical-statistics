import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

def set_ax(ax):
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ###设置右边坐标轴的粗细


color = ['orangered', 'g', 'blue', 'k']
df = pd.read_csv("../data-final.csv")
# df = df.dropna()
print(df.columns)
plt.figure(figsize=(16, 8))
# ---------百分比vs乳酸(实验组)----------------
ax1 = plt.subplot(1, 2, 1)

df1 = df[["脓毒症组IL-6", "脓毒症组IL-6对照组"]]
df1 = df1.dropna()
ax1.boxplot([df1["脓毒症组IL-6"], df1["脓毒症组IL-6对照组"]], notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['脓毒症组', '非脓毒症组'], fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel("IL-6(pg/ml)", fontsize=20)
x1, x2 = 1, 2
y, h, col = 80, 3, 'k'
ax1.set_ylim(0, 100)
ax1.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax1.text((x1+x2)*.5, y+h+0.5, "$P=.032$", ha='center', va='bottom', color=col, fontsize=20)
ax1.set_title("(a)", y=-0.2, fontsize=20)
set_ax(ax1)

# -----------百分比vsPCT(对照组)--------------
ax4 = plt.subplot(1, 2, 2)

df4 = df[["脓毒症存活组IL-6", "脓毒症死亡组IL-6"]]
df4 = df4.dropna()
ax4.boxplot([df4["脓毒症存活组IL-6"], df4["脓毒症死亡组IL-6"]], notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['存活组', '死亡组'], fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel("IL-6(pg/ml)", fontsize=20)
x1, x2 = 1, 2
y, h, col = 56, 3, 'k'
ax4.set_ylim(0, 70)
ax4.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax4.text((x1+x2)*.5, y+h+0.5, "$P=.579$", ha='center', va='bottom', color=col, fontsize=20)
ax4.set_title("(b)", y=-0.2, fontsize=20)
set_ax(ax4)

plt.show()
