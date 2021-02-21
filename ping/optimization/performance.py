import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv("./out.csv")
x = [0, 5, 10, 15, 20, 25, 30, 35, 38]
plt.xlabel("行业数量")
plt.ylabel("延时(ms)")
plt.plot(x, df["0"], color='red', label='累计0', lw=1)
plt.plot(x, df["100"], color='green', label='累计100', lw=1)
plt.plot(x, df["200"], color='blue', label='累计200', lw=1)
plt.plot(x, df["400"], color='olive', label='累计400', lw=1)
plt.plot(x, df["1000"], color='orange', label='累计1000', lw=1)
plt.legend(loc='upper left')
plt.title('延时随行业数量变化')
plt.show()