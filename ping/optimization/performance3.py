import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(50, 20))
df = pd.read_csv("./out3.csv")
df = df.sort_values(by='appointment_timestamp')
plt.xlabel("行业数量")
plt.ylabel("延时(ms)")
plt.xticks()
plt.xticks(df["appointment_timestamp"], df['us_time'], rotation='vertical')
plt.plot(df["appointment_timestamp"], df["live_count"], color='red', label='累计0', lw=1)
plt.title('延时随行业数量变化')
plt.show()