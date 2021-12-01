'''
# ##########################################
# VARIABLES PRACTICE:
# Here we shall practrice uage of Variables
#############################################
'''

import matplotlib.pyplot as plt
import pandas as pd

climate_change = pd.read_csv (r'C:\Users\Burudani\Documents\mainPythonFolder_v1\SpreadsheetFiles\climate_change.csv',
parse_dates=['date'])

#climate_change['date']= pd.to_datetime(climate_change['date'])
print(climate_change['date'].dtypes)
climate_change.set_index(['date'])
fig, ax = plt.subplots()



ax.plot(climate_change.index, climate_change['co2'])
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)')
plt.show()