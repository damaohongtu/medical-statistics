import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
def set_ax(ax):
    ax.spines['bottom'].set_linewidth(2);  ###���õײ�������Ĵ�ϸ
    ax.spines['left'].set_linewidth(2);  ####�������������Ĵ�ϸ
    ax.spines['right'].set_linewidth(2);  ###�����ұ�������Ĵ�ϸ
    ax.spines['top'].set_linewidth(2);  ###�����ұ�������Ĵ�ϸ

day = []
temperature = []
x = [0, 5, 10, 15, 20, 25, 30, 35, 38]
y = [0, 5, 10, 15, 20, 25, 30, 35, 38]
plt.xlabel("��ҵ����")
plt.ylabel("��ʱ(ms)")
plt.plot(x, y, color='red', label='�ۼ�0', lw=1)
plt.legend(loc='upper left')
plt.title('��ʱ����ҵ�����仯')
plt.show()