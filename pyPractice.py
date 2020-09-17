"""
===========================================================================================
FUNCTIONS PRACTICE:
The purpose of this file is to be a place to put down useful code for usage later.
This file as whole is not meant to be run, but rather its meant to be a place to pic code
  for running and modifying in the python scratch paper file
===========================================================================================
  """


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

"""READING_FILES"""
"""Notes: new line character'\n' is considered a white space and can therefore be stripped """
#fahndler is the file handler
fhandler= open('rwaki.txt')
for txtLine in fhandler:
    txtLine=txtLine.rstrip() # strips out the extra \n that the print statement will add automatically later
    print (txtLine)
    #NB this e

for txtLine in fhandler:
    if txtLine.startswith('From: '):
        print(txtLine)

for txtLine in fhandler:
    txtLine=txtLine.rstrip()
    if not txtLine.startswith('From: '):
        continue #skips lines that don't start with 'from'
    print(txtLine)

for txtLine in fhandler:
    txtLine=txtLine.rstrip()
    if not '@uct.ac.za' in txtLine:
        continue #skips lines that don't have '@uct.ac.za' in them
    print(txtLine)

fhandlerName= input ('Enter file name: ')
fhandler = open(fhandlerName)
count = 0
for line in fhandler:
    if line.startswith('Subject: ')  :
        count = count + 1
print('There were ', count, 'subject lines in ', fhandlerName)

#adding exception to deal with bad file names

fhandlerName= input ('Enter file name: ')
try:
    fhandler = open(fhandlerName)
except:
    print('File cannot be opened:', fhandlerName)
    quit()

count = 0
for line in fhandler:
    if line.startswith('Subject: ')  :
        count = count + 1
print('There were ', count, 'subject lines in ', fhandlerName)

"""LISTS"""
list.sort()  # arranges list elements in alphabetical order

numlist = list()
while True:
    inp = input('Enter a number:' )
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average =  sum(numlist) /len(numlist)
print('Average:' , average)

wordstring = 'with three words'  # create a list
wordstring.split() # splits a string to make a list according to white space

## NB: you can provide an argument for the split command e.g

wordstring.split(',')  #  splits entire string based on commas and returns a list based on that

x = range(6)  # create a 'Sequence' of values from 0 to 5

"""DICTIONARIES"""
purse = dict()   #purse is a new dictionary
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 75

print(purse)

#output is {'money': 12, 'candy': 3, 'tissue': 75}

counts = dict()  #counts is a new dictionary
names = ['csev', 'cwen', 'csev' , 'zqian' , 'cwen' ]
for name in names:
    if name not in names :
        counts[name] =  1
    else :
        counts[name] = counts[name] + 1
print(counts)
#output is {'csev' :2, 'zgian' :1, 'cwen': 2}

#alternative example:-

counts = dict()  #counts is a new dictionary
names = ['csev', 'cwen', 'csev' , 'zqian' , 'cwen' ]
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

#counting a pattern, in  this siutation we are readinging in a text file, going line by lne splitting and adding ther new words
# to a dictionary
counts = dict()
print('Enter a line of text : ')
line = input('')
words = line.split

print('Number of words is :' ,words)

print('counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

counts.keys()  # gives us the first identifying value of the dictionary
counts.values() # gives us the values only, not the keys of the dictionary
counts.items()  #gives us all keys and values in a dictionary

"""LOOPING THROUGH DICTIONARIES  TO PRINT ALL VALUES"""

jjj = {'chuck' : 1 , 'fred' : 42, 'jan' : 100}
for aaa,bbb in jjj.items():
    print (aaa,bbb)

#Result:-

# jan 100
# chuck 1
# fred 42

#Getting largest value in dictionary

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

"""TUPLES"""
# Its basically a list that uses parenthesis instead of square brackets
# AND is immutable(i.e cannot be changed once made)
# are like list but you use parenthesis BUT you don't need the parenthesis e.g x,y=3,4
# are a limited or efficient form a of list that you cannot modify
# if you use the items() method in a dictionary you will get a list of tuples
# i.e  a list of key - value pairs.
# In the alphabet, python considers letters to be more significant(higher in value the
# further along it is in the alphabet e.g A is less than B  therefore
# the highest value in the alphabet is the letter Z
# Tuples can BE sorted, but you can sort a dictionary
# Dictionaries have a sort function called 'SORTED' not SORT

x= ('glen', 'sally', 'joseph')
print(x[2]) #prints 'Joseph', just like in a list, notice the square bracket

d=dict()
d['csev'] = 2
d['cwen'] = 4



for (k,v) in d.items():  #items gives you the contents of the tuples or dictionary
    print(k,v)
#prints
# csev 2
# cwen 4

# you can assign tuples e.g

(x,y) = (4, 'fred')

#  To  sort a  dictionary of tuples  AND it sorts by keys only

d = {'a' : 10, 'b':1, 'c': 22}
t = sorted (d.items())

#you can also print out the sorted version of this( sorts by key only)

for k,v in sorted(d.items()):
    print(k,v)


# also for comparisons, tuples only check the significant digits first,if that checks out
# it ignores the rest

(0,1,2) < (5,1,2)

#to reverse a sort:-

# create an empty list first:-
tmp = list()

# then just add the values of the dictionary as normal to the list:-
for k,v in c.items()  :
     tmp.append((v,k))


# to sort the new list:-

tmp = sorted( tmp, reverse = True)
# what the above does is take the now reversed list and now sort it in reverse!!


