import pandas as pd

data = {'Name': ['Karan james', 'Rohit sing', 'Sahil nation', 'Aryan land'],
        'Age': [23, 22, 21, 24],
        'University': ['BHU', 'JNU', 'DU', 'BHU'],}

df = pd.DataFrame(data)

# Specify the file path where you want to save the Excel file
excel_file_path =  r'C:\Users\Burudani\Documents\mainPythonFolder_v1\SpreadsheetFiles\boldExample_v1.xlsx'

# Use ExcelWriter to create the Excel file
with pd.ExcelWriter(excel_file_path, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')

    # Access the workbook and the active sheet
    workbook = writer.book
    sheet = writer.sheets['Sheet1']

    # Remove existing filters (reset filters)
    sheet.auto_filter.ref = None

    # Apply filters to each column
    for col_num, col_letter in enumerate(sheet.iter_cols(min_col=0, max_col=len(df.columns)), start=0):
        sheet.auto_filter.ref = sheet.dimensions
        #sheet.auto_filter.add_filter_column(col_num, list(df[df.columns[col_num - 1]]))
    # Clear filters before saving the sheet
  

print(f"DataFrame has been saved to {excel_file_path} with filters applied to each column.")
