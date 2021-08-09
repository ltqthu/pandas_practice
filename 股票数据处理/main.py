import pandas as pd
df = pd.read_csv('sh.000001.csv', sep=',')

print(df)
print(df.iloc[0][0])
print(df.iloc[0][1])

print(df[(df['close2']-df['open2'])/df['open2'] > 0.05]['date'])
