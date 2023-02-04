# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
def set_ax(ax):
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['top'].set_linewidth(2)

color = ['orangered', 'g', 'blue', 'k']
df = pd.read_csv("../20210326-final.csv")
print(df.columns)
plt.figure(figsize=(8, 8))

size = 2

mymodel = [df["病例组第1天乳酸"].dropna(), df["第3天乳酸"].dropna()]
baseline = [df["对照组第1天乳酸"].dropna(), df["第3天乳酸.1"].dropna()]

# mymodel = np.asarray([[0.9184840801316903,0.9090443033011008,0.112511745951522], [0.9, 0.2, 0.1], [0.9, 0.2, 0.6, 0.44]])
mymodel_mean = [np.mean(x) for x in mymodel]
print(mymodel_mean)
# baseline = np.asarray([[0.188029597255012,0.18750779175862263,0.18768301416163474], [0.4, 0.3, 0.23], [0.11, 0.22, 0.33]])
baseline_mean = [np.mean(x) for x in baseline]

x = np.asarray([0, 1])

total_width, n = 0.3, 2
width = total_width / n
x = x - (total_width - width) / 2

plt.figure(figsize=(8, 6.5))
plt.grid(True, ls='--')
plt.ylim(0, 4)
# b1 = plt.boxplot(mymodel, widths=0.1, positions=x, notch=False, sym='o', vert=True)
b1 = plt.plot(x, mymodel_mean, '-')
# b2 = plt.boxplot(baseline, widths=0.1, positions=x+width, notch=False, sym='o', vert=True, patch_artist=True)
b2 = plt.plot(x, baseline_mean, '-')

plt.xticks(x+width/2,["Precision", "Recall"])
# for b in b1+b2:
#     h=b.get_height()
#     plt.text(b.get_x()+b.get_width()/2,h,'%0.3f'%float(h),ha='center',va='bottom')

plt.legend()
plt.savefig("./test.png", format='png',bbox_inches='tight')
plt.show()