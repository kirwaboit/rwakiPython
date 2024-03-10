import os
import win32com.client

sXlFile = r'C:\Users\Burudani\Documents\mainPythonFolder_v1\SpreadsheetFiles\excelMacroBook.xlsm'
xl=win32com.client.Dispatch("Excel.Application")
xl.Workbooks.Open(os.path.abspath(sXlFile))
try:
  xl.Run("populate_D2.ScriptforD2")
except Exception as e:
  print(e)

xl.Application.Quit() # Comment this out if your excel script closes
del xl