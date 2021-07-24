import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
#import datetime

plt.style.use('ggplot')

date_cols = ['Date']
df1 = pd.read_excel(r"C:\Users\Burudani\Documents\Finance_Trending\Checking_Jan1st2021_March10th2021.xlsx",
parse_dates = date_cols, # you can pass in a single value or a list of values
index_col = 'Date',
na_values= None) # specify how to deal with blank values


fig, ax = plt.subplots()
ax.bar(df1.index,df1['Amount'], color = "b",label="Money") # using bar instead of plot this time

#df1 = df1.groupby(df1['Date'].dt.month,as_index=True,sort=False)['Amount'].sum()
#df2 = df2.fillna('')
#df1.reset_index(drop=True, inplace = True)
#print(df1)
#print (df1.info())

#print(df1.columns)
# x = [datetime.datetime(2021,1,1),
#     datetime.datetime(2021, 2, 1),
#     datetime.datetime(2021, 3, 1)]
# y = [4, 9, 2]

#ax = plt.subplot()
# ax.bar(x, df2, width=10)
#ax.bar(df1.index, df2 )
# ax.xaxis_date()

#plt.show()
#df1.plot()
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.show()
