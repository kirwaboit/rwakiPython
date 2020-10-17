# Python Notes

A parameter is  a variable used in a function definition
e.g  
`<def my_first_function(my_first_parameter)>`   



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
therefore it can be used to skip certain lines of code

- Lists can have lists in them too e.g [1,2,[4,5],6]

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

- A class  is like a facrory for creating objects

- A method behaves like a function but it is invoked on a specific instance.

- Methods are accessed using dot notation   e.g the append() nethod below used on a list

        fruits = ['apple', 'banana', 'cherry']
        fruits.append("orange")

- A good example of a famous method is the __init__ function

- A parameter is a variable in a method definition. When a method is called, the arguments are the data you pass into the method's parameters. Parameter is variable in the declaration of function. Argument is the actual value of this variable that gets passed to function.

- This is why 'exampleList.append(7)' has 2 parameters even though you may think it only has one: the list stored in the variable 'exampleList' is the first parameter value and 7 is the second.

- A method does not need any other parameter information to do its work, there is still one formal parameter, <mark>self</mark>. As we stated earlier, all methods defined in a class that operate on objects of that class will have <mark>self</mark> as their first parameter. Again, this serves as a reference to the object itself which in turn gives access to the state data inside the object.

Linked logo: ![alt text](wordpress-logo-32.png)
(http://wordpress.com/ "WordPress Website")

<pre><code>This is a code block.
</code></pre>

