import matplotlib.pyplot as plt

# Set the data
labels = ['Fast Food', 'Alcohol', 'Helping People']
amounts = [1000, 500, 600]

# Calculate the percentages
total = sum(amounts)
percentages = [amount/total*100 for amount in amounts]

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(amounts, labels=labels, autopct='%1.1f%%')

# Add a title
ax.set_title('Spending for April')

# Show the chart
plt.show()