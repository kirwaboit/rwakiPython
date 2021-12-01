import json
import pandas as pd
  
# Opening JSON file
with open(r'C:\Users\Burudani\Documents\mainPythonFolder_v1\JSON\payDescriptionConverter.json') as json_file:
    expenditure_data = json.load(json_file)
  
    # Print the type of data variable
    print("Type:", type(expenditure_data))
  
    # # Print the data of dictionary
    # print("\nPeople1:", data['people1'])
    # print("\nPeople2:", data['people2'])

# Convert Dictionary to uppercase
expenditure_data = {k.upper():v.upper() for k,v in expenditure_data.items()}

# load the financial data into a data frame
date_cols = ['Date']
df1 = pd.read_excel(r"C:\Users\Burudani\Documents\Finance_Trending\Checking_Jan1st2021_March10th2021.xlsx",
parse_dates =date_cols, # you can pass only  a list of values
#index_col = 'Date',
na_values= None) # specify how to deal with blank values




#convert the dataframe column to capital letters
df1['Description'] = df1['Description'].str.upper()

#df1['Type']= df1['Description'].map(expenditure_data)

pattern = '|'.join(r"\b{}\b".format(x) for x in expenditure_data.keys())
df1['type'] = df1['Description'].str.extract('('+ pattern + ')', expand=False).map(expenditure_data)

for col in df1.columns:
    print(col)

df1 = df1.groupby(df1['Date'].dt.to_period('M')).sum()
df1 = df1.resample('M').asfreq().fillna(0)

df1.plot(kind='bar')


# # create  the name of the file
# file_name = 'datatoCheck_v5.xlsx'
  
# # saving the excel
# df1.to_excel(file_name)
# print('DataFrame is written to Excel File successfully.')
