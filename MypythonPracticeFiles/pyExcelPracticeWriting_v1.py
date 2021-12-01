import pandas as pd
import numpy as np
import re
#import win32com.client


# initialize list of lists 
data = [['tom', 10], ['nick', 15], ['juli', 14]] 
  
# Create the pandas DataFrame 
df = pd.DataFrame(data, columns = ['Name', 'Age']) 

# pass dataframe to df
df2transfer =df



fileoutputname = r'C:\Users\Burudani\Documents\rwakiExampleForExcel_v2.xlsx'   # shift + right click on folder/directory
with pd.ExcelWriter(fileoutputname) as writer:
    df2transfer.to_excel(writer, sheet_name = 'SHeet1', index = False, header = True)


m =re.search('\w.xlsx',fileoutputname)
print('The name of the file is ', m.group(0))




# macroPath = os.path.expanderuser(r'path to .xmls file with macros')
#  xl = win32com.client.Dispatch('Excel.Application')


#  workbook =  xl.workbooks.Open(Filename = macroPath, ReadOnly = 1)
#  xl.workbooks.Open(fileoutputname, ReadOnly = 1)
#  xl.Application.Run("VBAMacrotesting.xmls!Module2.Drills_macro")
