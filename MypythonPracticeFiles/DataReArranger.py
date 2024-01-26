import pandas as pd

# Load the Excel spreadsheet into a pandas DataFrame
file_path = r'C:\Users\Burudani\Documents\mainPythonFolder_v1\SpreadsheetFiles\example_spreadsheet_for_translator.xlsx'
df = pd.read_excel(excel_file)

# Extract the desired columns and rows
columns_to_extract = ['A', 'C', 'E', 'G']
rows_to_extract = range(1, 8)  # Rows 1 to 7

# Initialize an empty DataFrame to store the result
result_df = pd.DataFrame()

# Extract and append the columns to the result DataFrame
for col in columns_to_extract:
    extracted_data = df.loc[rows_to_extract, col].reset_index(drop=True)
    result_df[col] = extracted_data

# Print the resulting DataFrame
print(result_df)