import pandas as pd
import numpy as np
import matplotlib

#Bring in original Data sheet
df1 = pd.read_excel(r"C:\Users\Burudani\Documents\Finance_Trending\Checking_Jan1st2021_March10th2021.xlsx")  
#df1.columns = ['Date','Amount','Description']
#print(df1.head())
df1.columns = df1.columns.str.strip()

# Bring in the excell sheet that you will use to create the final column
df2 = pd.read_excel(r"C:\Users\Burudani\Documents\Finance_Trending\bank_amount_guide.xlsx") 

df2.columns = df2.columns.str.strip()


#df = df.assign(model2='Expenses')

#df.loc[:,'model2'] = str('Expenses')


#df['model2'] = 'Expenditure'
checkList = ["BANANA REPUBLIC PAYMENT","CHECK","DE POST PAID DET BILL PAY ","GEICO PREM COLL ","JPMorgan Chase Ext Trnsfr","CHASE CREDIT CRD AUTOPAY ","LOCKHEED MARTIN DIR DEP","MACYS PAYMENT","MONEY TRANSFER","NELNET LOAN","NORDSTROM PAYMENT","OVERDRAFT FEE","PAYPAL INST XFER","Amazon Digit","Amazon web service","Amazon Prime","wal-mart","tom thumb","7-eleven","aero café","goody goody","wave","txtag","Prime Video","cash app","mcdonald","cortland","apple","35413","uber eats","uber","netflix","at&t","Linux Academy","medium","hour fitness","Zelle from"]
checkListUppercase = [x.upper() for x in checkList]
#if(row.make1.upper() in checkListUppercase):

def NameReplacer(row):
    '''This Function replaces the long version of the transactional data with a short form version of it'''
    
    for item in checkListUppercase:
        if(item in row.Description.upper()):

            return item


df1.loc[:, 'Transaction'] = df1.apply(NameReplacer, axis = 1)  # apply the namereplacer function to the dataframe to create a new row: Transaction
#print (df1)

df1.Transaction.fillna(value=np.nan, inplace=True)   # replaces None values with NaN values

df1['Transaction'] = df1['Transaction'].fillna('EXPENDITURE')  # this allows you to now replace the NaN values with anything you want
#df['modelchecker'].replace(NaN, "", inplace=True)

#df['Match_Tester'] = df.apply(lambda errorDetector : df, axis = 1)
#print(df1)

#df1.groupby(['Transaction']).sum()
df1 = df1.drop('Description', axis = 1)
df1 = df1.drop('Date', axis = 1)

#print(df1)
for col in df1.columns:
    print(col)

df1.groupby(['Transaction']).sum().reset_index()

# for col in df2.columns:
    # print(col)
print(df1)

#df2.to_excel(r"C:\Users\Burudani\Documents\Finance_Trending\Checking_Jan1st2021_March10th2021_results3.xlsx",index = False)

df1.to_csv(r"C:\Users\Burudani\Documents\Finance_Trending\Checking_Jan1st2021_March10th2021_results5.xlsx")