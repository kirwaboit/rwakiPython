import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from an Excel file
df = pd.read_excel(r"G:\My Drive\Finances\Latest_Statement_March_2023_edited.xlsx", sheet_name='Sheet1')

# Group the data by month and category and compute the mean of the amount column
df['date'] = pd.to_datetime(df['date'])  # Convert date column to datetime format
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