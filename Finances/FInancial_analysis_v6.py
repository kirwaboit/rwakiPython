import pandas as pd
import openpyxl
import json
import tkinter as tk
from tkinter import filedialog
import datetime as dt

# Load the lookup table from the JSON file
with open(r'C:\Users\Burudani\Documents\mainPythonFolder_v1\JSON\payDescriptionConverter.json', 'r') as f:
    lookup_table = json.load(f)

# Create a tkinter root window
root = tk.Tk()

# Hide the root window
root.withdraw()

# Open a file dialog window to select the CSV file
file_path = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])

# Load the CSV file into a pandas dataframe
df = pd.read_csv(file_path)
# Load the Excel file into a Pandas dataframe
#df = pd.read_excel(r"G:\My Drive\Finances\Latest_Statement_April_2023.xlsx")

# Delete the unwanted 3rd and 4th columns (they have unecessary information in them)
df.drop(df.columns[[2, 3]], axis=1, inplace=True)


# Rename the remaining columns with new headers
df.columns = ['date', 'amount', 'Description']

# Define the column to search and the column to create
search_col = 'Description'
create_col = 'Category'


# Loop through the rows of the DataFrame and apply the lookup
for index, row in df.iterrows():
    for key in lookup_table.keys():
        if key in str(row[search_col]):
            df.loc[index, create_col] = lookup_table[key]
            break
    else:
        df.loc[index, create_col] = "NO CATEGORY"
# Get the current date in the format YYYY-MM-DD
current_date = dt.datetime.now().strftime('%Y-%m-%d')

# Create the new file name with the current date
new_file_name = 'Latest_Financial_Expenditure_Statement_' + current_date + '.xlsx'

# Save the dataframe to the new file name and location
df.to_excel(r"G:/My Drive/Finances/" + new_file_name, index=False)
# Save the updated dataframe to the Excel file
#df.to_excel(r"G:\My Drive\Finances\Latest_Statement_March_2023_edited.xlsx", sheet_name='Sheet1',index=False)
print ("Done")