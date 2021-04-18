import kirwaExampleModule as kem

#print(kem.var1)

print (kem.produceThis(3,4))


# exec("def init(self):\n\tprint(self.__class__.__name__ + \" created!\")")
# A = type('A', (), {'__init__' : init })
# a = A()


from inspect import getmembers, isfunction

#print(getmembers(kem, isfunction))

#help(kem)clear

