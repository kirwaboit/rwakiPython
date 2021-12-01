import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({"year": [1,1,1,1,2,3,2,3,2,3],
                   "month": [4, 6, 7, 5, 4, 6, 7, 1, 1, 4],
                   "value": list(range(5,15))})

print(df)
sns.barplot(data=df, y='value', x='year', hue='month')

plt.show()