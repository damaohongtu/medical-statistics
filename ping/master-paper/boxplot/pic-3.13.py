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
# ----------百分比vs乳酸(对照组)---------------
ax1 = plt.subplot(1,2,1)
df3 = df[["脓毒症组TNF-α", "脓毒症组TNF-α对照组"]]
df3 = df3.dropna()
ax1.boxplot([df3["脓毒症组TNF-α"], df3["脓毒症组TNF-α对照组"]], notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['脓毒症组', '非脓毒症组'], fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel("TNF-α(pg/ml)", fontsize=20)
x1, x2 = 1, 2
y, h, col = 750, 20, 'k'
ax1.set_ylim(0, 850)
ax1.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax1.text((x1+x2)*.5, y+h+0.5, "$^{*}P=.166$", ha='center', va='bottom', color=col, fontsize=20)
ax1.set_title("(a)", y=-0.2, fontsize=20)
set_ax(ax1)

ax7 = plt.subplot(1, 2, 2)
df3 = df[["脓毒症存活组TNF-α", "脓毒症死亡组TNF-α"]]
df3 = df3.dropna()
ax7.boxplot([df3["脓毒症存活组TNF-α"], df3["脓毒症死亡组TNF-α"]], notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['存活组', '死亡组'], fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel("TNF-α(pg/ml)", fontsize=20)
x1, x2 = 1, 2
y, h, col = 800, 20, 'k'
ax7.set_ylim(0, 880)
ax7.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax7.text((x1+x2)*.5, y+h+0.5, "$P=.608$", fontsize=20, ha='center', va='bottom', color=col)
ax7.set_title("(b)", y=-0.2, fontsize=20)
set_ax(ax7)

plt.show()
