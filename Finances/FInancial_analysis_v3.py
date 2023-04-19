import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create the DataFrame with random data
jan_dates = pd.date_range(start='2022-01-01', end='2022-01-31', periods=3)
feb_dates = pd.date_range(start='2022-02-01', end='2022-02-28', periods=3)
mar_dates = pd.date_range(start='2022-03-01', end='2022-03-31', periods=3)

categories = ['fast-food', 'entertainment', 'rent']

jan_data = [{'date': np.random.choice(jan_dates), 'amount': np.random.randint(10, 101), 'category': category} for category in categories]
feb_data = [{'date': np.random.choice(feb_dates), 'amount': np.random.randint(10, 101), 'category': category} for category in categories]
mar_data = [{'date': np.random.choice(mar_dates), 'amount': np.random.randint(10, 101), 'category': category} for category in categories]

df = pd.concat([pd.DataFrame(jan_data), pd.DataFrame(feb_data), pd.DataFrame(mar_data)], ignore_index=True)

# Group the data by month and category and compute the mean of the amount column
grouped_data = df.groupby(['date', 'category'])['amount'].mean().reset_index()

# Create the bar chart
sns.set_style("whitegrid")
sns.set_palette("bright")
ax = sns.barplot(x=grouped_data['date'].dt.strftime('%b'), y="amount", hue="category", data=grouped_data)

# Set the plot title and labels
plt.title("Grouped Bar Chart of Data by Month and Category")
plt.xlabel("Month")
plt.ylabel("Amount")

# Show the plot
plt.show()