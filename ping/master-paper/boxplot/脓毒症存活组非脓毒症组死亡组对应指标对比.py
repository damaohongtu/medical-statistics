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
ax1 = plt.subplot(2, 4, 1)
df1 = df[["脓毒症存活组单核细胞PD-L1百分比（%）", "脓毒症死亡组单核细胞PD-L1百分比（%）"]]
df1 = df1.dropna()
ax1.boxplot([df1["脓毒症存活组单核细胞PD-L1百分比（%）"], df1["脓毒症死亡组单核细胞PD-L1百分比（%）"]], notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['存活组', '死亡组'], fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel("单核细胞PD-L1百分比", fontsize=20)
# 绘制比较线
x1, x2 = 1, 2
y, h, col = 100, 3, 'k'
ax1.set_ylim(0, 120)
ax1.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax1.text((x1+x2)*.5, y+h+1, "$^{*}P=.917$", ha='center', va='bottom', color=col, fontsize=20)
ax1.set_title("(a)", y=-0.2, fontsize=20)
set_ax(ax1)

# ----------百分比vs乳酸(对照组)---------------
ax2 = plt.subplot(2, 4, 2)
df2 = df[["脓毒症存活组血乳酸", "脓毒症死亡组血乳酸"]]
df2 = df2.dropna()
ax2.boxplot([df2["脓毒症存活组血乳酸"], df2["脓毒症死亡组血乳酸"]], notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['存活组', '死亡组'], fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel("血乳酸", fontsize=20)
x1, x2 = 1, 2
y, h, col = 10, 0.5, 'k'
ax2.set_ylim(0, 14)
ax2.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax2.text((x1+x2)*.5, y+h+0.5, "$^{*}P=.057$", ha='center', va='bottom', color=col, fontsize=20)
ax2.set_title("(b)", y=-0.2, fontsize=20)
set_ax(ax2)

# ----------百分比vsPCT(实验组)---------------
ax3 = plt.subplot(2, 4, 3)
df3 = df[["脓毒症存活组PCT", "脓毒症死亡组PCT"]]
df3 = df3.dropna()
ax3.boxplot([df3["脓毒症存活组PCT"], df3["脓毒症死亡组PCT"]], notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['存活组', '死亡组'], fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel("PCT", fontsize=20)
x1, x2 = 1, 2
y, h, col = 118, 3, 'k'
ax3.set_ylim(0, 140)
ax3.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax3.text((x1+x2)*.5, y+h+0.5, "$^{*}P=.000$", ha='center', va='bottom', color=col, fontsize=20)
ax3.set_title("(c)", y=-0.2, fontsize=20)
set_ax(ax3)

# -----------百分比vsPCT(对照组)--------------
ax4 = plt.subplot(2, 4, 4)

df4 = df[["脓毒症存活组IL-6", "脓毒症死亡组IL-6"]]
df4 = df4.dropna()
ax4.boxplot([df4["脓毒症存活组IL-6"], df4["脓毒症死亡组IL-6"]], notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['存活组', '死亡组'], fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel("IL-6", fontsize=20)
x1, x2 = 1, 2
y, h, col = 56, 3, 'k'
ax4.set_ylim(0, 70)
ax4.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax4.text((x1+x2)*.5, y+h+0.5, "$^{*}P=.579$", ha='center', va='bottom', color=col, fontsize=20)
ax4.set_title("(d)", y=-0.2, fontsize=20)
set_ax(ax4)

ax5 = plt.subplot(2, 4, 5)
df1 = df[["脓毒症存活组IL10", "脓毒症死亡组IL10"]]
df1 = df1.dropna()
ax5.boxplot([df1["脓毒症存活组IL10"], df1["脓毒症死亡组IL10"]], notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['存活组', '死亡组'], fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel("IL10", fontsize=20)
# 绘制比较线
x1, x2 = 1, 2
y, h, col = 580, 20, 'k'
ax5.set_ylim(0, 680)
ax5.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax5.text((x1+x2)*.5, y+h+1, "$^{*}P=.715$", ha='center', va='bottom', color=col, fontsize=20)
ax5.set_title("(e)", y=-0.2, fontsize=20)
set_ax(ax5)

# ----------百分比vs乳酸(对照组)---------------
ax6 = plt.subplot(2, 4, 6)
df2 = df[["脓毒症存活组IL1β", "脓毒症死亡组IL1β"]]
df2 = df2.dropna()
ax6.boxplot([df2["脓毒症存活组IL1β"], df2["脓毒症死亡组IL1β"]], notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['存活组', '死亡组'], fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel("IL1β", fontsize=20)
x1, x2 = 1, 2
y, h, col = 85, 3, 'k'
ax6.set_ylim(0, 100)
ax6.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax6.text((x1+x2)*.5, y+h+0.5, "$^{*}P=.394$", ha='center', va='bottom', color=col, fontsize=20)
ax6.set_title("(f)", y=-0.2, fontsize=20)
set_ax(ax6)

# ----------百分比vsPCT(实验组)---------------
ax7 = plt.subplot(2, 4, 7)
df3 = df[["脓毒症存活组TNF-α", "脓毒症死亡组TNF-α"]]
df3 = df3.dropna()
ax7.boxplot([df3["脓毒症存活组TNF-α"], df3["脓毒症死亡组TNF-α"]], notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['存活组', '死亡组'], fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel("TNF-α", fontsize=20)
x1, x2 = 1, 2
y, h, col = 750, 20, 'k'
ax7.set_ylim(0, 880)
ax7.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax7.text((x1+x2)*.5, y+h+0.5, "$^{*}P=.608$", fontsize=20, ha='center', va='bottom', color=col)
ax7.set_title("(g)", y=-0.2, fontsize=20)
set_ax(ax7)
# 脓毒症存活组非脓毒症组死亡组对应指标对比
plt.savefig("./outcome/脓毒症存活组和脓毒症死亡组对比.png")
plt.show()
