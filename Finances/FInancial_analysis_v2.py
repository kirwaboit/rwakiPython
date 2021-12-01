#################################################################
## This code is for analysing my pay slip
##   
#################################################################

'''IMPORTS'''
import pandas as pd
import numpy as np
import json

import matplotlib.pyplot as plt
import seaborn as sns

from timeit import default_timer as timer
'''VARIABLES'''
payConverter = {}
keepList = ['fast_food','alcohol','shopping','groceries','streaming_movies_and_music','entertainment']
keepList = [x.upper() for x in keepList] 
print(keepList)

'''FUNCTIONS'''
#def payType(data):
def payType(row):
    global payConverter
    count = 0
    #print('here is the payconverter :',payConverter)
    '''This function searches for a match in a first column then creates a new column with a result to that match to form the categories column'''
    for key, value in payConverter.items():
        #print (key,'checking in', row)
       
        # count = count + 1
        # if count  == 20 :
        #     break
        if key in row:
            #print('found match')
            return value
           
        
        #print(key, '->', payDict[key])
        
    # if re.match(r'^[A-Z]{3};[A-Z]{3}\d{10}',row):
    #     return 'serial match found'
    # else:
    #     return 'No match here'
def cleanData():
    '''This function makes the data easier to visualize '''
    df1.columns = df1.columns.str.upper()
    df1.columns = [x.strip().replace(' ','_') for x in df1.columns]
    df1['DATE'] = df1['DATE'].dt.to_period('M')
   

def prepJson():
    global payConverter
    json_file_path = 'JSON/payDescriptionConverter.json'  # REMEMBER
    with open(json_file_path, 'r') as j:
        payConverter = json.loads(j.read())
    payConverter = {k.upper():v.upper() for k,v in payConverter.items()} # turns all items to capital letters
        

def expenditureExtractor(row):
    if row < 0:
        return abs(row)

# def dropUnimportantRows(row):
#     global keepList 
#     print('This is the row I am comparing', row)
#     if row not in keepList:
#         df1.drop([row])





     
    
    #print(payConverter)

  
    
    


'''LOAD DATA'''
df1 = pd.read_excel(r"Finances/Checking_Jan1st2021_Oct19th2021.xlsx") 
#df1.transaction.apply(lambda x: x.astype(str).str.upper()) #convert all the values in the transaction column to capital letters
#df1.transaction.apply(lambda x: str(x).upper()) #convert all the values in the transaction column to capital letters
df1['transaction'] = df1['transaction'].str.upper()
#df1.columns = ['Date','Amount','Description']
#print(df1.head())


'''MAIN FUNCTION'''
def main():
    '''Main function'''
    cleanData()
    prepJson()
    fig, ax = plt.subplots()
    df1.loc[:, 'CATEGORY'] = df1.TRANSACTION.apply(payType)
    df1.loc[:, 'EXPENDITURE'] = df1.AMOUNT.apply(expenditureExtractor)
    #df2 = df1.CATEGORY.apply(dropUnimportantRows)
    # df2 = df1[df1.CATEGORY in keepList]
    df2 = df1.query('CATEGORY in @keepList')

    #dfObj['z'] = dfObj['z'].apply(np.square)
    df2.to_excel(r"Finances/Checking_Jan1st2021_Oct19th2021_results_v4Truncated.xlsx", index = False)
    sns.set(font_scale= 0.7)
    # sns.set_theme(style="darkgrid")
    sns.set_style(style="darkgrid")
    sns.barplot(data=df2, y='EXPENDITURE', x='DATE', hue='CATEGORY',ci=None, estimator=sum)
    
    for container in ax.containers:
        ax.bar_label(container)
    plt.show()

  
  
    
start = timer()
if __name__ == "__main__":
    main()

end = timer()
print('Your second code took ', end-start ,' Seconds')
