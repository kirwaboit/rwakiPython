import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame([['g1','c1',10],['g1','c2',12],['g1','c3',13],['g2','c1',8],
                   ['g2','c2',10],['g2','c3',12]],columns=['group','column','val'])


df.pivot("column", "group", "val").plot(kind='bar')
df.pivot("month", "group", "val").plot(kind='bar')
print(df)

plt.show()