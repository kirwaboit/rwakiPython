#Helen Boit
#Problem 5
x = 0

def readFile():
    with open(r"C:\Users\Burudani\Documents\mainPythonFolder_v1\Helen_Python\exchange-rate.txt",'r') as infile:
        countries= [line.rstrip() for line in infile]
        print(*countries,'\n')
        #print(*countries, sep = '\n')
        
    
    for i in range(len(countries)):
        countries[i] = countries[i].split(",")
        # convert numeric looking strings to numeric values
        countries[i][2] = float(countries[i][2])
    #print (countries[0][0])
    return countries


   
        
        
def main ():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("This program asks for two countries on the display list")
    print("and the amount of currency you want to convert from the ")
    print("first country to the second country. It will then display")
    print("the final amount in the currency of the second country")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    tempList = []
    amount=0
    countries = readFile()
    #tempList,amount= getInputs(countries)
                  #tempList,amount=tempList,amount
    #print(tempList,amount)
                   #exchange(tempList,amount)
   

main() 






