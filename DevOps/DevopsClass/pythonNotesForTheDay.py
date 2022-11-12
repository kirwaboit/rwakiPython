x = 0

def readFile():
    with open(r"C:\Users\Burudani\Documents\mainPythonFolder_v1\Helen_Python\exchange-rate.txt",'r') as infile:
        countries= [line.rstrip() for line in infile]  # now has one continuous line of values
                                  
        print(*countries)                              # has been unpacked to 
        print(*countries, sep = '\n')
        
    
    for i in range(len(countries)):
        countries[i] = countries[i].split(",")
        '''convert numeric looking strings to numeric values'''
        countries[i][2] = float(countries[i][2])
        print (countries[i][2])
    return countries


   
        
        
def main ():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("This program parses through data in a txt file")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    tempList = []
    amount=0
    countries = readFile()
  
   

main() 
