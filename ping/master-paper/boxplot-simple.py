# 导入包
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']


color = ['orangered','g','blue','k']
ds = pd.read_csv("./boxplot-scatter-spearman-new.csv")
ds = ds.dropna()
print(ds.columns)

tang_array = ds[['A-单核细胞PD-L1百分比（%）', 'A-血乳酸mmol/L', 'A-CRP', 'A-PCT']]

fig = plt.figure(figsize=(8, 6))

f, (ax, ax2) = plt.subplots(2, 1, sharex=True)

f1 = ax.boxplot(tang_array, notch=False, sym='o', vert=True)
f2 = ax2.boxplot(tang_array, notch=False, sym='o', vert=True)
for box, c in zip(f1['boxes'], color):
    box.set(color=c)    # 箱体边框颜色
for box, c in zip(f1['medians'], color):
    box.set(color=c)    # 箱体边框颜色
for box, c in zip(f2['boxes'], color):
    box.set(color=c)    # 箱体边框颜色
for box, c in zip(f2['medians'], color):
    box.set(color=c)    # 箱体边框颜色
# zoom-in / limit the view to different portions of the data
ax.set_ylim(140, 230)  # outliers only
ax2.set_ylim(0, 53)  # most of the data

# hide the spines between ax and ax2
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax2.spines['right'].set_visible(False)
# ax.xaxis.tick_top()
ax.xaxis.set_visible(False)
ax.tick_params(labeltop='off')  # don't put tick labels at the top
ax2.xaxis.tick_bottom()

d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
# ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
# ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# 绘制比较线
x1, x2 = 1, 2
y, h, col = 145, 3, 'k'
ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax.text((x1+x2)*.5, y+h+1, "$^{*}P=.556$", ha='center', va='bottom', color=col)

# 绘制比较线
x1, x2 = 2, 3
y, h, col = 210, 3, 'k'
ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax.text((x1+x2)*.5, y+h+1, "$R^{2}=ax+b$", ha='center', va='bottom', color=col)

plt.xticks([x+1 for x in range(4)], ['单核细胞PD-L1百分比(%)', '血乳酸mmol/L', 'CRP', 'PCT'])

plt.show()