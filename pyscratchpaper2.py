class ExampleClass:
            exampleVar1 = 32  # Class variable
            def __init__(self, parameter1: int,parameter2: str,parameter3: str ,parameter4: float )-> str:   # any placeholder here in this constructor is called a parameter
                self.number = parameter1   # self.name is an instance variable
                self.string1 = parameter2
                self.string2 = parameter3
                self.double = parameter4
            def __str__(self):  #this method allows us to create the 
                return 'Your values are number {} with word {} and word {} and number {}.' .format(self.number,self.string1,self.string2,self.double)  
                
                
#We just randomly generate some values to feed into the class, these variables are refered to as "arguaments" if used in a function call/method call/class call
argument1 = 1
argument2 = 3
argument3 = 'world'
argument4 = 2.0

ExampleInstance = ExampleClass(argument1,argument2,argument3,argument4)


print(ExampleInstance)  # print the string in the method  "__str__"