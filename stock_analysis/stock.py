import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei']  
# Matplotlib中设置字体-黑体，解决Matplotlib中文乱码问题
plt.rcParams['axes.unicode_minus'] = False    
# 解决Matplotlib坐标轴负号'-'显示为方块的问题
sns.set(font='SimHei')                        
# Seaborn中设置字体-黑体，解决Seaborn中文乱码问题
df = pd.read_csv('sh.000001.csv')
time=[]
range=[]
for i in np.arange(-0.1,0.09,0.01):
    print(i <= (df['close2']-df['open2'])/df['open2'] < (i+0.01))
    lenth=0#len(df[i <= (df['close2']-df['open2'])/df['open2'] and (df['close2']-df['open2'])/df['open2'] < (i+0.01)])
    time.append(lenth)
    range.append(i)
# print(time)
plt.figure(figsize=(20, 10), dpi=100)
plt.plot(range,time,marker = 'o',markersize = 6)
plt.xlabel("涨跌幅度", fontdict={'size': 16})
plt.ylabel("天数", fontdict={'size': 16})
plt.title("股票涨跌分析", fontdict={'size': 20})
plt.show()