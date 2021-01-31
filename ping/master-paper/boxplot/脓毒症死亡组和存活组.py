import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

color = ['orangered', 'g', 'blue', 'k']
df = pd.read_csv("../data-final.csv")
print(df.columns)

def set_ax(ax):
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ###设置右边坐标轴的粗细



# ---------百分比vs乳酸(实验组)----------------
ax1 = plt.subplot(2, 2, 1)
df1 = df[["脓毒症存活组单核细胞PD-L1百分比（%）", "脓毒症组血乳酸mmol/L"]]
df1 = df1.dropna()
ax1.boxplot(df1, notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['单核细胞PD-L1百分比(%)', '血乳酸mmol/L'])
plt.yticks(fontsize=20)
# 绘制比较线
x1, x2 = 1, 2
y, h, col = 120, 3, 'k'
ax1.set_ylim(0, 160)
ax1.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax1.text((x1+x2)*.5, y+h+1, "$^{*}P=.000$", ha='center', va='bottom', color=col, fontsize=20)
ax1.set_title("(a)存活组", y=-0.35, fontsize=20)
set_ax(ax1)

# ----------百分比vs乳酸(对照组)---------------
ax2 = plt.subplot(2, 2, 2)
df2 = df[["脓毒症死亡组单核细胞PD-L1百分比（%）", "脓毒症死亡组血乳酸"]]
df2 = df2.dropna()
ax2.boxplot(df2, notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['单核细胞PD-L1百分比(%)', '血乳酸mmol/L'])
plt.yticks(fontsize=20)
x1, x2 = 1, 2
y, h, col = 78, 3, 'k'
ax2.set_ylim(0, 110)
ax2.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax2.text((x1+x2)*.5, y+h+0.5, "$^{*}P=.094$", ha='center', va='bottom', color=col, fontsize=20)
ax2.set_title("(b)死亡组", y=-0.35, fontsize=20)
set_ax(ax2)

# ----------百分比vsPCT(实验组)---------------
ax3 = plt.subplot(2, 2, 3)
df3 = df[["脓毒症存活组单核细胞PD-L1百分比（%）", "脓毒症组PCT"]]
df3 = df3.dropna()
ax3.boxplot(df3, notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['单核细胞PD-L1百分比（%）', 'PCT'])
plt.yticks(fontsize=20)
x1, x2 = 1, 2
y, h, col = 120, 3, 'k'
ax3.set_ylim(0, 160)
ax3.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax3.text((x1+x2)*.5, y+h+0.5, "$^{*}P=.000$", ha='center', va='bottom', color=col, fontsize=20)
ax3.set_title("(c)存活组", y=-0.35, fontsize=20)
set_ax(ax3)

# -----------百分比vsPCT(对照组)--------------
ax4 = plt.subplot(2, 2, 4)

df4 = df[["脓毒症死亡组单核细胞PD-L1百分比（%）", "脓毒症存活组PCT"]]
df4 = df4.dropna()
ax4.boxplot(df4, notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['单核细胞PD-L1百分比（%）', 'PCT'])
plt.yticks(fontsize=20)
x1, x2 = 1, 2
y, h, col = 120, 3, 'k'
ax4.set_ylim(0, 160)
ax4.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax4.text((x1+x2)*.5, y+h+0.5, "$^{*}P=.015$", ha='center', va='bottom', color=col, fontsize=20)
ax4.set_title("(d)死亡组", y=-0.35, fontsize=20)
set_ax(ax4)

plt.show()
