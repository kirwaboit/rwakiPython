import pandas

file_path = r'C:\Users\Burudani\Documents\mainPythonFolder_v1\SpreadsheetFiles\example_spreadsheet.xlsx'
df = pd.read_excel(file_path, parse_dates=['date'])

# Convert the 'date' column to the format 'YYYYMMDD'
df['date'] = df['date'].dt.strftime('%Y%m%d')

# Process each row to create the output strings with the updated date format
output_strings = []

for _, row in df.iterrows():
    # Constructing the string as per the provided instructions, with updated date format
    output_string = f"{row['location']}_GERMAN{row['dataflightno']}_FR{row['flno']}K{row['bno']}{row['date']}_789.csv"
    output_strings.append(output_string)

# Output strings
for string in output_strings:
    print(string)