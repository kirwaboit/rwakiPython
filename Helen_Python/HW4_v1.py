#Helen Boit
#Problem 4

def getInputs(presList,presDict):
    convertToDict (presList)
    while True:                
        lowerNumber =input("Enter the lower number for the range:\t")
        isNumber (lowerNumber)
        upperNumber =input("Enter the upper number for the range:\t")
        isNumber (upperNumber)
        print ('Final value: ',isNumber (upperNumber))
        
        
        
        if upperNumber >= lowerNumber:
            for value in presDict.keys():
                if presDict[value] >= lowerNumber and presDict[value] <= upperNumber:
                    print (presDict[value],value)
            break 
        else:
            print ("Please enter a lower bound first, then an upper bound!")
            continue
def isNumber (num):
    validFirstChars = ["0","1","2","3","4","5","6","7","8","9"]
    validChars = ["0","1","2","3","4","5","6","7","8","9"]
    if num[0] not in validFirstChars:
         print ("{} is not a valid number. Please enter numbers between 1 and 45.".format(num[0]))
         return True
     
    if num.count(".") >= 1:
        print()
        print("you entered decimals. Please only enter numbers between 1 and 45.")
        return False
     
    for ch in num[1:]:
         if ch not in validChars:
             print ()
             print ("{} is not a valid number".format(ch))
             return False
             
         # All characters are valid characters
    return True

def convertToDict (presList):
    presDict = {}
    counter = 0
    for item in presList:
        if item not in presDict:
            counter +=1
            presDict.update({item:counter})     
    return(presDict)


##def displayOutputs (presDict):

    #while True:        
        #lowerNumber =int(input("Enter the lower number for the range:\t"))
        #upperNumber =int(input("Enter the upper number for the range:\t"))

##        if upperNumber >= lowerNumber:
##            for value in presDict.keys():
##                if presDict[value] >= lowerNumber and presDict[value] <= upperNumber:
##                    print (presDict[value],value)
##                    break 
##        else:
##            print ("Please enter a lower bound first, then an upper bound!")
##            continue
                
def main ():
    presList = []
    print("Who were the Presidents in your range?\n")    
    with open(r"C:\Users\Burudani\Documents\mainPythonFolder_v1\Helen_Python\USPres.txt", "r") as infile:
        presList = [line.rstrip() for line in infile]    
        #print (presList)
    presDict = {}
    convertToDict(presList)
    getInputs(presList,presDict)    
 #   displayOutputs(presDict)
main ()