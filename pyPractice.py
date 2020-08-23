"""FUNCTIONS PRACTICE"""


def my_first_function(my_first_parameter):  # you can call the parameter
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


def computepay(h,r):
    if h<= 40:
        return (h*r)
    else:
        return ((40*r)+((h-40)*(r*1.5)))


# hrs = input("Enter Hours:")
# hrs=float(hrs)
# rate = input("Enter rate:")
# rate=float(rate)
# p = computepay(hrs,rate)
# print("Pay",p)


"""LOOP HOMEWORK 5.0"""

# while True:
#     # line=input('Enter Value >')
#     line = 'done'
#     if line =='done':
#         break    # break mean exit the loop immediately!!!
#     else:
#         line="not done"
#     print(line)
# print('Done! ')
#
#
# """LOOP EXAMPLE_v1 5.3"""
# valueToCompare=-45
# for items in [9,41,12,3,74,15]:
#     if items>valueToCompare:
#         valueToCompare=items
# print ("The highest value is" , valueToCompare)

"""LOOP EXAMPLE_v2 5.3"""
#
# num = 0
# tot =0.0
# while True:
#     # sval = input('Enter a number')
#     sval = 'done'
#     if sval == 'done':
#         break
#     try:
#         fval = float(sval)
#     except Wrong:
#         print('Invalid input')
#         continue   # if exception is met, go to top of que
#     num = num +1
#     tot = tot + fval
# print(tot, num,tot/num)

"""LOOP EXAMPLE_v3 5.3"""

# largest = None
# smallest = None
# initializeInputFlag=0  # zero means th inputs have not been inittilized
# while True:
#     # num = input("Enter a number: ") #TODO remove comment to run this code properly
#     num = 'done'
#     if num == "done": break
#     # print(num)
#     try:
#         num=float(num)
#     except:
#         print('Invalid input')
#         continue
#     if initializeInputFlag==0:
#         largest=num
#         smallest=num
#         initializeInputFlag = 1
#
#     if largest<num:
#         largest=num
#     if smallest>num:
#         smallest=num
#
#
# print("Maximum is", int(largest))
# print("Minimum is", int(smallest))

"""STRING LOOP EXAMPLE 6.1"""
'''loop through the length of the string and print all the values of the string'''

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

'''Using  a good short form of a loop we can reduce ths loop to :-'''
fruit = 'banana'
for item in fruit:
    print(item)


# result: it prints 'b a n a n a'

'''Slicing strings'''

s= 'Monty Python'
print(s[0:4])

# result is: Mont

s= 'Monty Python'
print(s[:2])  # print the beginning  until index 2 ie "Mo"
print(s[8:])  # print from index 8 till the end i.e "thon"
print(s[:])   # print everything

'''Finding stuff in strings'''
fruit = 'banana'

if 'n' in fruit:
    print('found n')

'''METHODS IN CLASS STR'''
print(fruit.upper())

print(fruit.capitalize())

print(fruit.find('na'))  # returns first index of where it found a value

print(fruit.replace('a','O'))  #works for replacign strings to e.g replace('bob','ken'),

#  .lstrip  strips left space, .rstrip, or .strip

#line.startswitch('please')

"""STRING PROJECT"""

text = "X-DSPAM-Confidence:    0.8475"

atpos=text.find('0')
print(atpos)

print(text[23:])

numbaStr1=float(text[23:])

print(numbaStr1)

atpos=text.find('0')

numberStr=text[23:]

floatnmbr=float(numberStr)

print(floatnmbr)