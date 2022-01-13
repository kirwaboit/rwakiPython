﻿---
page_type: sample
description: "This sample consists of a Python web application that invokes common Microsoft Graph security API calls."
products:
- ms-graph
languages:
- python
- html
extensions:
  contentType: samples
  technologies:
  - Microsoft Graph
  services:
  - Security 
  createdDate: 4/5/2018 3:22:33 PM
---
# Python Notes

![language:Python](https://img.shields.io/badge/Language-Python-blue.svg?style=flat-square) ![license:MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)  
Welcome! this is a repo containing files for practicing python and other programming languages 
## Table of Contents  
- [1.TODO](#1-todo)
    - [1.1 Use cases](#11-usecases)
    - [1.2 Best Practices](#12-best-practices)
        - [1.2.1 At Home](#121-at-home)  

DRY - Don't Repeat Yourself, concept for re-using code

# Vscode Tips

- Select current word =  ctrl + D  
- Select all instances of that word = ctrl + shft + L

# Markdown tips
- How to add new line in Markdown presentation?  
- To force a line return, place two empty spaces at the end of a line.   
- For code just use 4 spaces
- for Colored text use this template <span style="color:orange">some *orange* text</span>.   
- Great Markdown guide [Markdown Guide: Basic Syntax](https://www.markdownguide.org/basic-syntax/).
\\( and \\)
- For html picture links...avoid using the `align` function e.g `align = left`  this messes up how markdown is viewed in several editors

## Image Examples
<img src="bash/images/bashDarkLogo.png" alt="drawing" width="400" height="174"/>   
<img src="bash/images/interactivePic.drawio.svg" alt="drawing" align="left" width="800" height="374"/>  
<img src="https://code.visualstudio.com/assets/updates/1_63/notebook-file-links.gif" alt="drawing" width="800" height="374"/>  


# Git Operations
## Git pushing 

git add .  
git commit -m "description/reason for this commit"  
git push -u "url_of_project" master  

e.g  
git push -u "https://gitlab.com/rwaki/rwakipythonpractice.git" master

Pushing with a token

git push "https://gitlab-ci-token:accessTokenHere@gitlab.com/rwaki/rwakipythonpractice.git" master 


##



# Git Badges

https://docs.gitlab.com/ee/user/project/badges.html

# Git Notes  
To write code in-line use the backtick  e.g  `this is my code`  
To write code use tripple backticks to mark to open and close the code block, like this:-  
``` 
My Block of code

and other stuff 
```



## Setting up git clone(copy) for the first time
git clone git@github:me/name.git .

git clone https://gitlab.com/janevieve/myterraformproject.git .    
git clone https://gitlab.com/rwaki/aws_rwakiterraform.git .

## Submitting changes

git add .  
git commit -m "description/reason for this commit"  
git push -u "https://gitlab.com/janevieve/myterraformproject.git" master    

git push https://gitlab-ci-token:zsan6XdkBsLQ9sDsSnky@gitlab.com/rwaki/rwakipythonpractice.git" master  

git clone https://gitlab.com/janevieve/myterraformproject.git .

git remote add origin https://gitlab.com/rwaki/repoforindex.git

git clone https://gitlab.com/rwaki/rwakipythonpractice.git .


## Useful python tips
- continue means STOP and immediately go back to start of loop,  
therefore it can be used to skip certain lines of code e.g

-Strive to use single quotation marks when you can

- Lists can have lists in them too e.g 

        [1,2,[4,5],6]

- Easy quick "for" loop 

        for i in range(2):  
        print "hello" 
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

- It is therefore correct to be referring to the instance  as the thing you create from the class rather than the object. What you work with, is the instance

- A method behaves like a function but it is invoked on a specific instance.

- Methods are accessed using dot notation   e.g the append() method below used on a list

        fruits = ['apple', 'banana', 'cherry']
        fruits.append("orange")

- A good example of a famous method is the __init__ function, commonly referred to then as a the __init__ method. (The usually refer to this as "dunder init", much in the same way  __main__ is referred to as "dunder main", or __name__ as "dunder name". Basically the double undeerscores are refred to as "dunders")

- Class Variables — Declared inside the class definition (but outside any of the instance methods). They are not tied to any particular object of the class, hence shared across all the objects of the class. Modifying a class variable affects all objects instance at the same time.

- Instance Variable — Declared inside the constructor method of class (the __init__ method). They are tied to the particular object instance of the class; hence the contents of an instance variable are completely independent from one object instance to the other.

- A parameter is a variable in a method definition. When a method is called, the arguments are the data you pass into the method's parameters. Parameter is variable in the declaration of function. Argument is the actual value of this variable that gets passed to function. 

- The Example below demonstrates a class with parameters, how they are related to arguments and how they are used with instance variables within the class 

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

# Summary on Try/Except use cases
- Use it when the code has a strong chance to error out, but still want it to do something!   
useful that is important.   

Linked logo: ![alt text](wordpress-logo-32.png)
(http://wordpress.com/ "WordPress Website")

<pre><code>This is a code block.
</code></pre>

# Fixing bad runners   - in windows
- First off I had several issues, one was that I tried to install several git runners in my system
- So first step was to delete ALL the runner except for the single one that you need, I mean obliterate all files relating to git-lab runners in your entire machine
- Now delete all services related to previously installed gitlab-runners in your windows services i.e  type services in your windows search bar, enter it and check to see if you have a gitlab-runner service either running or stopped.
- To delete this service open up an administrator command prompt and type "sc delete gitlab-runner" after that is done, you gitlab-runner should no longer show up in your services
- Now go to your folder, the one where you want you gitlab-runner installed and do a fresh intall and registration in that folder!
- Make sure your gitlab runner has the correct tags, AND make sure your gitlab repo project has the same tags that you want you runner to respond to 
- NB:  when dealing with gitlab runner you will want to run and do changes to your gitlab runner in "administrative mode" in the cmd teminal .Therefore you want your vscode, or pycharm or cmd or git terminal, or IDE of choice to have administrative priviledges for the cmd terminal. If you don't do that , it may deny access to some commands.
testing glr


## Terminal Colors

    print("\033[31mThis is red font.\033[0m")
    print("\033[32mThis is green font.\033[0m")
    print("\033[33mThis is yellow font.\033[0m")
    print("\033[34mThis is blue font.\033[0m")
    print("\033[38mThis is the default font. \033[0m")  # More than 37 will display the default font.

df[df['Country (region)'].str.match('^P.*')== True]
df['Country (region)'].str.match('^P.*')== True



## Questions for ivy

1. Hi So I talk to a couple  of people I have been helping , I like to ask them these questions (it's always nice to have alot of good friends in this area)
2. Tell me a bit more about this internship who is it with and for how long?, are you getting paid?  what tasks are they giving you ? anything with power BI? or just Sql pulls
   1. internship free
3. Have you sent out you resume to start getting job offers?
   1. 12000 IN A YEAR
4. Have you had any interviews so far?  how did they go , did you get any offers and for how much?
5. What are your most difficult challenges at this moment in time? e.g understanding sometype of grouping sql code, DAX scripts in power BI etc, or answerign certain interview questions
6. Do you discuss your work currently with your classmates?

6. Is your sister still considering going back into data science

7. Finaly if there is anythign I can do to assist you please let me know, ty!
8. I am proud of the progress you have made!!! umetoka mbali!! and you have achieved alot

ivy.njoroge@gmail.com

​	

