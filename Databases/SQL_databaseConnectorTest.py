
'''In this example I connect to an SQL Server hosted locally on my machine '''

import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-Q8DKIFQ;'
                      'Database=LydiaHelp;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM LydiaHelp.dbo.companies')

# for row in cursor:
#     print(row)

#print(pyodbc.drivers())
print(*pyodbc.drivers(), sep='\n')