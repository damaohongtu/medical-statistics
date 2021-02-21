import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv("./out2.csv")
x = [0, 100, 200, 400, 1000]
plt.xlabel("累计数量")
plt.ylabel("延时(ms)")
plt.plot(x, df["1"], color='red', label='行业数1', lw=1)
plt.plot(x, df["5"], color='green', label='行业数5', lw=1)
plt.plot(x, df["10"], color='blue', label='行业数10', lw=1)
plt.plot(x, df["15"], color='olive', label='行业数15', lw=1)
plt.plot(x, df["20"], color='orange', label='行业数20', lw=1)
plt.plot(x, df["25"], color='black', label='行业数25', lw=1)
plt.plot(x, df["30"], color='pink', label='行业数30', lw=1)
plt.plot(x, df["35"], color='purple', label='行业数35', lw=1)
plt.plot(x, df["38"], color='c', label='行业数38', lw=1)


plt.legend(loc='upper left')
plt.title('延时随行业数量变化')
plt.show()