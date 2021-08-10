import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('data/sh.000001.csv', sep=',')

# 找出上证指数当日涨幅超过5%的日期
daily_incr = (df['close2']-df['open2'])/df['open2']
date = df[daily_incr > 0.05]['date']
print(date)

# 绘制当日涨幅的分布图
plt.figure()
plt.hist(daily_incr, bins=50)
plt.show()

