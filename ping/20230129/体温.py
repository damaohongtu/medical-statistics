import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
def set_ax(ax):
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ###设置右边坐标轴的粗细

day = []
temperature = []
x = [0, 5, 10, 15, 20, 25, 30, 35, 38]
y = [0, 5, 10, 15, 20, 25, 30, 35, 38]
plt.xlabel("行业数量")
plt.ylabel("延时(ms)")
plt.plot(x, y, color='red', label='累计0', lw=1)
plt.legend(loc='upper left')
plt.title('延时随行业数量变化')
plt.show()