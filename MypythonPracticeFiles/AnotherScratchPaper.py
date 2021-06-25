austin_weather['MONTH'],austin_weather['MLY-PRCP-NORMAL']
austin_weather['MONTH'],austin_weather['MLY-PRCP-NORMAL']
seattle_weather['MONTH'],seattle_weather['MLY-PRCP-NORMAL']
seattle_weather['MONTH'],seattle_weather['MLY-PRCP-NORMAL']


seattle_weather['MLY-PRCP-NORMAL'], color = 'b')
ax[0].plot(seattle_weather['MONTH'],seattle_weather['MLY-PRCP-25PCTL'], color = 'b', linestyle = '--')
ax[0].plot(seattle_weather['MONTH'],seattle_weather['MLY-PRCP-75PCTL'], color = 'b', linestyle = '--')

# Plot Austin precipitation data in the bottom axes
ax[1].plot(austin_weather['MONTH'],austin_weather['MLY-PRCP-NORMAL'], color = 'r')
ax[1].plot(austin_weather['MONTH'],austin_weather['MLY-PRCP-25PCTL'], color = 'r',linestyle = '--')
ax[1].plot(austin_weather['MONTH'],austin_weather['MLY-PRCP-75PCTL'], color = 'r',linestyle = '--')

plt.show()