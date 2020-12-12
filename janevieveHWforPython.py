'''
    Create list object with following student names.

	john, kelly, dave, mary, frank, nancy, paul,paul,kelly

	a. Write the code to reverse the list in python  
	b. Write code to remove duplicate items from the list  
	c.  Sort the names in ascending order  
	
     You will learn Variables, data types, data structures  

	**Two important Programmig principles**  
	DRY : Do not Repeat yourself    
	Better to be explicit then implicit
'''  


''' 1 A.Creating a List of strings'''

emptylist = ['']   #whitespace  
nameList = ['kirwa boit'] #string
kirwaBoit = 1*3
janevieveString = ''   
employeeName = 'james'
employeeCar = 'Hyundai'

studentNameList = ['john','kelly','dave', 'mary','frank','nancy','paul','paul', 'kelly'] 
studentNameList.reverse()

print('The Reversed list lookse like this: ',studentNameList)



'''1 B.Removing Duplicates'''


newStudentList = []  #this is going to  
for item in studentNameList: 
    if item not in newStudentList: 
        newStudentList.append(item)

print('List without duplicates',newStudentList)



''' 1 C.Sort the names in ascending order'''

newStudentList.sort()

print('sorted list: ',newStudentList)


''' 2 .Create a list of student records with this data. Use list of dictionary object to store all student records

    name: John
	city: dallas
	age: 21

	name: Kelly
	city: austin
	age: 22

	name: Mary
	city: austin
	age: 20

	name: Greg
	city: dallas
	age: 23
'''

thisdict1 = {
  'name':'John',
  'city':'dallas',
  'age': '21',
}

thisdict2 = {
  'name':'Kelly',
  'city':'austin',
  'age': '22',
}

thisdict3 = {
  'name':'Mary',
  'city':'austin',
  'age': '20',
}

thisdict4 = {
  'name':'Greg',
  'city':'dallas',
  'age': '23',
}


print('item from dictionary',thisdict1['city'])

dictionaryList = [thisdict1,thisdict2,thisdict3,thisdict4]

'''2a. Write the code to list the student names. Create a list *object* from all student names'''

   #  ctrl+/   for commenting/uncommenting multiple lines in a selection

dictNameList = []   

for dictionaryListitems in dictionaryList:
    dictNameList.append(dictionaryListitems['name'])


print(dictNameList)
 
   #for key,value in item.items():

# for key,value in dictionaryList.items():
#     print (key,value)

'''2b. Greg changes his city to "Atlanta". Update the dictionary object'''

thisdict4['city'] = 'atlanta'

print(thisdict4['city'])

'''2c. Print  all student names and their ages and create a List of the Name/Age pair'''

nameAgeList = []
for dictionaryListitems in dictionaryList:
    print(dictionaryListitems['name'],dictionaryListitems['age'])
    #tuple = (x,y)
    nameAgeList.append((dictionaryListitems['name'],dictionaryListitems['age']))



print('the final output for Q2 is: ',nameAgeList)

'''3. Generate list using range(). Specify start,stop and size of the range'''
print('this is in item',item)

x = range(3, 20,2)
#x= [3, 5,7,9.....]
for item in x:
  print(item)

'''4.Create a Python application with the following functionalties'''
'''a. It will take 5 numbers as inputs from the user '''
'''b. Prints all the 5 numbers'''

inputList = []
squareOfinput = [] 
rangeOfInputs = range(1,6)
for item in rangeOfInputs:
  try:
    inputFromUser = input("Enter a number:")
    inputFromUser = int(inputFromUser)
    inputList.append(inputFromUser) #append input from user
    squareOfinput.append((inputFromUser)**2) 
  except:
    print('element is not an integer, try again')



  


print("Elements in the list is are:",inputList)
'''c. Prints the largest number of the 5 '''

print("Largest element in the list is:", max(inputList)) 

'''d. Prints square of all the numbers'''
print("square of the elements in the list is:", squareOfinput) 

'''e. If the intake value is not an integer type, it will reject the value and ask 	the user to input an integer'''
print('done')










