
import glob
print("Hello World")


# Using '*' pattern 
print('\nNamed with wildcard *:')
#for name in glob.glob('/home/geeks/Desktop/gfg/*'):
path  = r'C:\Users\Burudani\Documents\mainPythonFolder_v1\SpreadsheetFiles\*.csv'
for name in glob.glob(path):
    print(name)