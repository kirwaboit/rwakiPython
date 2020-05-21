"""FUNCTIONS PRACTICE"""


def my_first_function(my_first_parameter):  #you can call the parameter
    if my_first_parameter == 'es':
        print('Hola')
    elif my_first_parameter == 'fr':
        print('Bonjour')
    else:
        print('Hello')


my_first_function('en')
my_first_function('es')
my_first_function('fr')


def addtwo(a, b):
    added = a + b
    return added


x = addtwo(3, 5)  # two arguments
print(x)

"""FUNCTIONS HOMEWORK 4.6"""

'''Write a program to prompt the user for hours and rate per hour using 
input to compute gross pay. Pay should be the normal rate for hours up to 
40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
Put the logic to do the computation of pay in a function called computepay() and 
use the function to do the computation. The function should return a value. Use 45 
hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float() to convert the string to a number.
 Do not worry about error checking the user input unless you want to - you can assume 
 the user types numbers properly. Do not name your variable sum or use the sum() function.'''


# def computepay(h,r):
#     if h<= 40:
#         return (h*r)
#     else:
#         return ((40*r)+((h-40)*(r*1.5)))
#
#
# hrs = input("Enter Hours:")
# hrs=float(hrs)
# rate = input("Enter rate:")
# rate=float(rate)
# p = computepay(hrs,rate)
# print("Pay",p)


"""LOOP HOMEWORK 5.0"""

while True:                 
    line=input('Enter Value >')
    if line =='done':
        break    #break mean exit the loop immediately!!!
    else:
        line="not done"
    print(line)
print('Done! ')


"""LOOP EXAMPLE 5.3"""
valueToCompare=-45
for items in [9,41,12,3,74,15]:
    if items>valueToCompare:
        valueToCompare=items
print ("The highest value is" , valueToCompare)
