# Python Notes

DRY - Don't Repeat Yourself, concept for re-using code



# Markdown tips
How to add new line in Markdown presentation?  
To force a line return, place two empty spaces at the end of a line.  
Great Markdown guide [Markdown Guide: Basic Syntax](https://www.markdownguide.org/basic-syntax/).

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

-Strive to use single quotation mmarks when you can

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

- A good example of a famous method is the __init__ function, commonly refferd to then as a the __init__ method.

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

# Summary on Class use cases

You can also use self-defined classes to hold data – for example, data you get from making a request to a **REST API**.

Before you decide to define a new class, there are a few things to keep in mind, and questions you should ask yourself:

- What is the data that you want to deal with? (Data about a bunch of songs from iTunes? Data about a bunch of tweets from Twitter? Data about a bunch of hashtag searches on Twitter? Two numbers that represent coordinates of a point on a 2-dimensional plane?)

- What will one instance of your class represent? In other words, which sort of new thing in your program should have fancy functionality? One song? One hashtag? One tweet? One point? The answer to this question should help you decide what to call the class you define.

- What information should each instance have as instance variables? This is related to what an instance represents. See if you can make it into a sentence. “Each instance represents one < song > and each < song > has an < artist > and a < title > as instance variables.” Or, “Each instance represents a < Tweet > and each < Tweet > has a < user (who posted it) > and < a message content string > as instance variables.”

- What instance methods should each instance have? What should each instance be able to do? To continue using the same examples: Maybe each song has a method that uses a lyrics API to get a long string of its lyrics. Maybe each song has a method that returns a string of its artist’s name. Or for a tweet, maybe each tweet has a method that returns the length of the tweet’s message. (Go wild!)

- What should the printed version of an instance look like? (This question will help you determine how to write the __str__ method.) Maybe, “Each song printed out will show the song title and the artist’s name.” or “Each Tweet printed out will show the username of the person who posted it and the message content of the tweet.”

After considering those questions and making decisions about how you’re going to get started with a class definition, you can begin to define your class.

Remember that a class definition, like a function definition, is a general description of what every instance of the class should have. (Every Point has an x and a y.) The class instances are specific: e.g. the Point with a specific x and y >. You might have a Point with an x value of 3 and a y value of 2, so for that particular instance of the class Point, you’d pass in 3 and 2 to the constructor, the __init__ method, like so: new_point = Point(3,2), as you saw in the last sections.

Linked logo: ![alt text](wordpress-logo-32.png)
(http://wordpress.com/ "WordPress Website")

<pre><code>This is a code block.
</code></pre>

