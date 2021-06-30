import matplotlib.pyplot as plt
import pandas as pd
#from datetime import datetime

climate_change = pd.read_csv(r'C:\Users\Burudani\Documents\mainPythonFolder_v1\SpreadsheetFiles\climate_change.csv',parse_dates = ['date_cc'])

def plot_timeseries(axes,x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)  
    axes.set_xlabel(xlabel)  
    axes.set_ylabel(ylabel, color=color)  
    axes.tick_params('y', colors=color)

fig, ax = plt.subplots()
plot_timeseries(ax, climate_change.index, climate_change['co2'],'blue', 'Time', 'CO2 (ppm)')

ts = pd.Timestamp(year = 2015,  month = 10, day = 6)
# Print the Timestamp object
print(ts.date())

ax2 = ax.twinx()
plot_timeseries(ax2, climate_change.index,climate_change['relative_temp'],'red','Time','Relative temperature (Celsius)') 
ax2.annotate(">1 degree",
xy=(ts.date(), 1),
xytext=(ts.date(), -0.2),
arrowprops={"arrowstyle":"->", "color":"gray"})
plt.show()