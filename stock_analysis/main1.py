import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sh.000001.csv")
x = (df['close2']-df['open2'])/df['open2']
print(plt.hist(x, bins=30))
plt.show()
