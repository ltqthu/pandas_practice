import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import wave
from matplotlib.pyplot import MultipleLocator
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False    
sns.set(font='SimHei')                        
df = pd.read_csv('data.csv')
x = (df['close2']-df['open2'])/df['open2']
y=df["date"]
# plt.figure(figsize=(10, 5), dpi=150)
# plt.plot(y,x,marker = 'o',markersize = 1)
# plt.xlabel("日期", fontdict={'size': 16})
# index_ls=list(range(1990,2021,3))
# scale_ls=range(11)
# ax=plt.gca()
# plt.xticks(scale_ls,index_ls)
# x_major_locator=MultipleLocator(500)
# ax.xaxis.set_major_locator(x_major_locator)
# print(index_ls)
# plt.ylim(-0.1,0.1)
# plt.ylabel("涨跌幅度", fontdict={'size': 16})
# plt.title("股票涨跌分析", fontdict={'size': 20})
# plt.show()
sig=np.array(x)
sig1=np.vstack((sig, sig))
sig1=sig1*1000000
sig1=sig1.astype(np.short)
print(sig1)
f= wave.open("stock's_wave.WAV","wb")
f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(1000)
f.writeframes(sig1.tobytes())
f.close()