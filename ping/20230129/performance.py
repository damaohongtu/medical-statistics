import matplotlib.pyplot as plt

def set_ax(ax):
    ax.spines['top'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    # ax.spines['right'].set_visible(False)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(16, 6))
ax1 = plt.subplot(3, 1, 1)
ax1_1 = ax1.twinx()

ax2 = plt.subplot(3, 1, 2)
ax2_1 = ax2.twinx()

ax3 = plt.subplot(3, 1, 3)
ax3_1 = ax3.twinx()

x0 = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44]
tem = [37.5, 37.5, 37.4, 37.4, 37.1, 37, 37.6, 37, 37.2, 37.4, 37.4, 37.3, 37, 36.8, 37, 37.1, 37.5]


# WBC(*10^9/L)
x1 = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
WBC = [4.58, 2.76, 4.42, 4.41, 6.58, 5.35, 6.37, 8.37, 11.91, 19.11, 15.78,	12.02, 9.8,	8.29, 7.94,	8.93, 6.59,	6.41, 7.19,	6.93, 7.07,	6.77, 4.98,	5.4, 6.2, 6.04,	7.04, 7.03,	9.32, 9.12,	11.7, 8.48,	8.25]

x2 = [12, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
PCT = [0.11, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.08, 0.11, 0.12, 0.08, 0.1, 0.12, 0.12, 0.12, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.25, 0.28, 0.13]

# IL-6(pg/ml)
x3 = [12, 18, 19, 20, 21, 24, 26, 27, 28, 31, 33, 34, 35, 43]
IL_6 = [110, 126, 68.8, 94.9, 874, 1100, 1100, 1100, 1100, 471, 338, 374, 434, 96.3]


# CRP
x4 = [12, 14, 16, 17, 18, 19, 20, 21, 24, 26, 27, 28, 31, 33, 34, 43]
CRP = [79.4, 37.2, 10.5, 5.6, 3.03, 1.78, 1.33, 0.9, 1.3, 2.27, 3.3, 8.28, 4.6, 6.2, 4.4, 167]

x5 = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
LB = [0.34, 0.44, 0.61, 0.42, 0.86, 0.82, 0.55, 0.63, 0.93, 0.83, 0.86, 0.9, 0.75, 0.78, 0.69, 0.72, 0.67, 0.92, 1.07, 1.31, 1.24, 0.98, 0.71, 0.73, 0.71, 0.73, 0.86, 0.96, 0.83, 1.15, 0.65, 0.75, 0.54]


ax1.set_ylim(36, 38)

set_ax(ax1)
set_ax(ax1_1)
line1 = ax1.plot(x0, tem, 'b--', marker='.', lw=1, label='体温')
line1_1 = ax1_1.plot(x5, LB, 'r--', marker='x', lw=1, label='淋巴细胞绝对值')
ax1_list = (line1[0], line1_1[0])
labels_1 = [name.get_label() for name in ax1_list]
ax1.legend(ax1_list, labels_1, loc='upper left')
ax1.set_ylabel("体温($^\circ$C)")
ax1_1.set_ylabel("淋巴细胞绝对值(*10^9/L)")
ax1.set_xticks([12, 15, 20, 30, 40, 44])
ax1.set_xticklabels(['12d', '15d', '20d', '30d', '40d', '44d'])


set_ax(ax2)
set_ax(ax2_1)
line2 = ax2.plot(x1, WBC, 'b--', marker='.', lw=1, label='WBC')
line2_1 = ax2_1.plot(x2, PCT, 'r--', marker='x', lw=1, label='PCT')
ax2_list = (line2[0], line2_1[0])
labels_2 = [name.get_label() for name in ax2_list]
ax2.legend(ax2_list, labels_2, loc='upper left')
ax2.set_ylabel("WBC(*10^9/L)")
ax2_1.set_ylabel("PCT(ng/ml)")
ax2.set_xticks([12, 15, 20, 30, 40, 44])
ax2.set_xticklabels(['12d', '15d', '20d', '30d', '40d', '44d'])


set_ax(ax3)
set_ax(ax3_1)
plt.xlabel("COVID-19发病后(天)")
line3 = ax3.plot(x3, IL_6, 'b--', marker='.', lw=1, label='IL-6')
line3_1 = ax3_1.plot(x4, CRP, 'r--', marker='x', lw=1, label='CRP')
ax3_list = (line3[0], line3_1[0])
labels = [name.get_label() for name in ax3_list]
ax3.legend(ax3_list, labels, loc='upper left')
ax3.set_ylabel("IL-6(pg/ml)")
ax3_1.set_ylabel("CRP(mg/L)")

ax3.set_xlabel("COVID-19发病后(天)")
plt.xticks([12, 15, 20, 30, 40, 44], ['12d', '15d', '20d', '30d', '40d', '44d'])

plt.show()
