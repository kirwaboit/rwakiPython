"""FUNCTIONS PRACTICE"""


def my_first_function(my_first_parameter):
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
