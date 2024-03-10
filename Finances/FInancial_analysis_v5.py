import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from an Excel file
df = pd.read_excel("G:\My Drive\Finances\Latest_Statement_March_2023_edited.xlsx", sheet_name='Sheet1')

# Group the data by month and category and compute the mean of the amount column
df['date'] = pd.to_datetime(df['date'])  # Convert date column to datetime format
grouped_data = df.groupby(['date', 'category'])['amount'].mean().reset_index()

# Get the top 5 categories by amount for each month
top5 = grouped_data.groupby('date').apply(lambda x: x.nlargest(5, 'amount')).reset_index(drop=True)

# Create the bar chart
sns.set_style("whitegrid")
sns.set_palette("bright")
ax = sns.barplot(x=top5['date'].dt.strftime('%b'), y="amount", hue="category", data=top5)

# Set the plot title and labels
plt.title("Top 5 Categories by amount per Month")
plt.xlabel("Month")
plt.ylabel("amount")

# Invert the y-axis to invert the positive and negative values
ax.invert_yaxis()

# Format the tooltip to show the amount and category
def format_tooltip():
    category = top5.loc['amount', 'category']
    return f"{amount},{category}"

plt.gca().format_ydata = format_tooltip

# Show the plot
plt.show()