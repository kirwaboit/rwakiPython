#Helen Boit
#Problem 5
x = 0
def readFile():
    with open(r"C:\Users\Burudani\Documents\mainPythonFolder_v1\Helen_Python\exchange-rate.txt",'r') as infile:
        countries= [line.rstrip() for line in infile]
        #print(countries)
        
    
    for i in range(len(countries)):
        countries[i] = countries[i].split(",")
        # convert numeric looking strings to numeric values
        countries[i][2] = float(countries[i][2])
    #print (countries[0][0])
    return countries

def getInputs(countries):
       
    while x == 0:
        
        first = input("\nEnter the name of the first country, or type Q and enter to quit:\t").upper()
        print(first)
        if first == 'first.upper()'
        second = input("Enter the name of the second country:\t").upper()
        print(second)        
        amount = float(input("Amount of money to convert:\t\t"))
      
        for i in range(len(countries)):
            if first == countries[i][0]:
                firstCurrency=countries[i][1]
                firstRate=countries[i][2]
                tempList.append(first)
                tempList.append(firstCurrency)
                tempList.append(firstRate)
            else:
                i = i +1
                
        for i in range (len(countries)):
            if second == countries [i][0]:
                secondCurrency =countries[i][1]
                secondRate = countries [i][2]
                tempList.append(second)
                tempList.append(secondCurrency)
                tempList.append(secondRate)
            else:
                i = i+1                
        #print(tempList,amount)
                
    return (tempList,amount)
        
        
            

def exchange(tempList,amount):
    
    tempList,amount = tempList,amount
    newAmount = 0   
    newAmount = (amount*(tempList[5]))/tempList[2]
    print(newAmount)
   
        
        
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
    tempList,amount= getInputs(countries)
    #tempList,amount=tempList,amount
    print(tempList,amount)
    #exchange(tempList,amount)
   

main ()
