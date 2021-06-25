'''SETUP'''
import pandas as pd
import matplotlib.pyplot as plt 
from datetime import datetime 
#import the dataframe and designate the data types:-


import matplotlib.pyplot as plt

climate_change = pd.read_csv (r'C:\Users\Burudani\Documents\mainPythonFolder_v1\SpreadsheetFiles\climate_change.csv',
fig, ax = plt.subplots()ax.plot(climate_change.index, climate_change['co2'])
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)')
plt.show()




date_cols = ['date_cc'] # Specifying columns to be treated as  a datetime datatype in the pandas dataframe
dtypes = [datetime, float,float] 
df_climate_change = pd.read_csv (r'C:\Users\Burudani\Documents\mainPythonFolder_v1\SpreadsheetFiles\climate_change.csv',
parse_dates=date_cols,
dtype={"co2": float,
"relative_temp": float})

for col in df_climate_change.columns:
    print(col)
print(df_climate_change['date_cc'].dtypes)

'''QUERY'''
#Setting a slicer/filter for a range of time
#df_climate_change.set_index(['date_cc'])
#sixties =  df_climate_change.loc["1960-01-01","1969-12-31"]
sixties =  df_climate_change[df_climate_change.date_cc.between('1960-01-01', '1969-12-31')]

fig, ax = plt.subplots()

print( 'this is the df',sixties)

#df_climate_change.set_index('date_cc')
# ax plots x-axis folowed by y-axis
ax.plot(sixties.index, sixties['co2'], marker =None, linestyle = None, color = "b")
ax.set_xlabel('Time')
ax.set_ylabel('Co2 (ppm)')
plt.show()
