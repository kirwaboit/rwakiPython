# Python Notes

DRY - Don't Repeat Yourself, concept for re-using code



# Markdown tips
How to add new line in Markdown presentation?  
To force a line return, place two empty spaces at the end of a line.  
test123  

# Git Notes

## Setting up git clone(copy) for the first time
git clone git@github:me/name.git .

git clone https://gitlab.com/janevieve/myterraformproject.git .  

## Submitting changes

git add .
git commit -m "description/reason for this commit"
git push -u "https://gitlab.com/janevieve/myterraformproject.git" master  


1. First item
2. Second item
3. Third item
4. Fourth item


## Useful python tips
- continue means STOP and immediately go back to start of loop,  
therefore it can be used to skip certain lines of code e.g

- Lists can have lists in them too e.g 

        [1,2,[4,5],6]

# Data Structures

- Strings are "immutable"  i.e it cannot be changed, need to a create
a new string to change the old one.

- Lists are "mutable" , you can change an element of a list using the 
index operator

- Dictionaries are a memory based key value store, they are associative arrays,most powerful data collection

- Unlike strings, dictionaries do not use indexes

- Tuples are immutable, just like strings, and thus can be more efficiently stored by python

- as a result you cannot sort, add, or reverse tuples

- Dictionaries and tuples go hand in hand, literally !!! as a dictionary is comprised of tuples

- Lists are a sequence, tuples are a sequence and even a string is a sequence so stuff like max() methods work on them

# Methods and classes

- A class is like a factory for creating objects, it is a blueprint for creating objects

- An instance is a unique copy of a Class that describes an Object.

-It is therfeore correct to be refering to the instance  as the thing you create from the class rather than the object. What you work with, is the instance

- A method behaves like a function but it is invoked on a specific instance.

- Methods are accessed using dot notation   e.g the append() method below used on a list

        fruits = ['apple', 'banana', 'cherry']
        fruits.append("orange")

- A good example of a famous method is the __init__ function

- Class Variables — Declared inside the class definition (but outside any of the instance methods). They are not tied to any particular object of the class, hence shared across all the objects of the class. Modifying a class variable affects all objects instance at the same time.

- Instance Variable — Declared inside the constructor method of class (the __init__ method). They are tied to the particular object instance of the class, hence the contents of an instance variable are completely independent from one object instance to the other.

- A parameter is a variable in a method definition. When a method is called, the arguments are the data you pass into the method's parameters. Parameter is variable in the declaration of function. Argument is the actual value of this variable that gets passed to function. 

- The Example below demonstrates  a class with parameters ,how they are related to arguments and how they are used with instance variables within the class 

        class ExampleClass:
            exampleVar1 = 32  # Class variable
            def __init__(self, parameter1,parameter2,parameter3):
                self.name = parameter1   # self.name is an instance variable
                self.population = parameter2
                self.state = parameter3
        
        ExampleInstance = ExampleCLass(argument1,argument2,argument3)

- This is why 'exampleList.append(7)' has 2 parameters even though you may think it only has one: the list stored in the variable 'exampleList' is the first parameter value and 7 is the second.

- A method does not need any other parameter information to do its work, there is still one formal parameter, <mark>self</mark>. As we stated earlier, all methods defined in a class that operate on objects of that class will have <mark>self</mark> as their first parameter. Again, this serves as a reference to the object itself which in turn gives access to the state data inside the object.

Linked logo: ![alt text](wordpress-logo-32.png)
(http://wordpress.com/ "WordPress Website")

<pre><code>This is a code block.
</code></pre>

