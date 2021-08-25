# What are we gonna learn?
# Today, we are gonna learn "Printing", "Commenting", "Debugging", "String Manipulation" and "Variables".
# We are also gonna learn how to make a "Simple Band Name Generator"!
# So lets get started!

# Printing to the console!
print("Hello World!") # This command prints whatever you type inside the parenthesis in the console!
# But you can see here, that we had not only typed the "Hello World!" inside the parenthesis, but also some quotation marks! It tells the computer that we don't have to print out the quotes!
# Now what are these quotes? Let's find out!

# Strings:

# These words which are inside the quotes, in programming languages are known as "strings"!
# You can imagine a "string" as a "string of beads" but instead, its a series of "letters" and the quotes indicate the "beginning" and the "ending" to the string.
# That is the reason, you need to be careful while rogramming!
# print("Hello World!) # If you remove the first "# " in this line, you can see that the last parentesis is also colored! This means that the string has not ended there and will result in an error!
# If you run the code as-it-is without fixing the "string issue", its gonna give you an error in the console.
# We will get into the "Errors" in the future!

## An interactive Coding Exercise 1 ##
# The coding exercise is given in this MD file: https://github.com/AaryanKhClasses/Learning-Python-new/tree/main/src/exercises/Coding_Exercise_1.md
# I know thats a long hyperlink, but most code editors allows you to "Ctrl+Click" to follow that link!
# I hope you have completed the exercise sincerely. Now lets move on.

# While completing the exercise, you can see the third "print" statement was as follows:
print("print('what to print')") # Why have we put a "single" quote inside the print statement inside the string? Why have we not put a "double" quote?
# Thats because, in python. The interpreter doesn't really care how you close a string. A string can be written insid a "double" quote as well as a "single" quote!
# Now, if I replace the single quotes with double quotes: (after removing the first "# ")
# print("print("what to print")") # It counts `print("print(` as one string and `")"` as a different one, completely excluding the middle part and the python think its actual code and trys to interpret it.
# But as its not valid code, python will give you an "error" if you try to run it!

# Now how to fix this?
# Commonly, you just replace the "double" quotes to "single" quotes or the other way around!
# But theres an another way to fix this which we will see afterwards!

# Multiple lines in a single string!
# Till now you saw, that if we want to print more than 1 line to the console, we need to put each line in a seperate print statement
# But, you can do this in a single line!
# This is done by the "\n" character.
print("Hello World!\nHow are you?") # This will print out the string "Hello World!" to the console and then "How are you?" in the second line.
# Remember that its a "\" and not a "/"

# Concatenating strings!
# This means thats you can add two different strings together!
# This is done by the "+" sign after a string.
print("Hello" + "World!") # This will print out the string "HelloWorld!" to the console.
# But, you will see that "Hello" and "World" are a single word.
# There are 2 ways to fix this.
# You can add a "space" after the first word (here, "Hello") OR before the second work (here, "World!")
print("Hello " + "World!") # This will print out the string "Hello World!" to the console, thus fixing the problem.
# You can also add a "third string" to fix this problem.
print("Hello" + " " + "World!") # This will also fix the problem.

# In python programming, "spaces" are really important.
# Not only in strings, but also at the begenning of each sentence.
# print('Hello World!') # If you remove the first "#" without the space after it, you will see that you have got an "IndentationError"
# This means that you have not indented the code properly. In simple words, it means that you have added a space at the starting of a line.
# To avoid this, just make sure that there is no space at the begenning of any line.

## An Interactive Coding Exercise 3 ##
# The coding exercise is given in this MD file: https://github.com/AaryanKhClasses/Learning-Python-new/tree/main/src/exercises/Coding_Exercise_2.md
# I hope you have completed the exercise sincerely. Now lets move on.

# The Input Function
# The input function is used to get input from the user.
# To do that, instead of using the print function, you can use the input function.
input('What is your name? ') # This will ask the user to enter a string and then print it out.
# The input function looks very similar to the print function.
# What can we use this for now?
# Whenever we input the string, it replaces the whole input statement with the string that you inputted.
# With this, we can print out the string with the input inside!
print("Hello " + input('What is your name? ')) # This will ask the user their name, and then print out "Hello " and the name inputted.

# Comments!
# This file literally has most of comments.
# This means, that the code will not get executed when ran.
# To comment a code, you need to have a "#" before the code you don't want to get executed.
# This code, will be ignored by the interpreter.

## An Interactive Coding Exercise 3 ##
# The coding exercise is given in this MD file: https://github.com/AaryanKhClasses/Learning-Python-new/tree/main/src/exercises/Coding_Exercise_3.md

# I hope you have completed the exercise sincerely. Now lets move on.

# Python variables
# A variable is a name that refers to a value.
str = input('Enter a string: ') # This will ask the user to enter a string, and will store the value in a variable called "str", which can be access later on.
print(str) # This will print out the value stored in the variable "str".

# Now, ask the name "variable" suggest, it something that can be varied, that is, changed
str = 'Hello World' # This will change the value stored in the variable "str" to "Hello World"
print(str) # This will print "Hello World" instead of the inputted value.

## An Interactive Coding Exercise 4 ##
# The coding exercise is given in this MD file: https://github.com/AaryanKhClasses/Learning-Python-new/tree/main/src/exercises/Coding_Exercise_4.md
# I hope you have completed the exercise sincerely. Now lets move on.

# Naming variables
# You can name a variable anything you want, but you should name your variables readable and understandable. Make your variables to be descriptive.
# You can also have two or more words in a same variable, example "user_name" or "userName".
# You can't add a space between the name of the variable and will give a SyntaxError.
# You also can have numbers in your variable names, but they can't be the first character of the variable.
# You should also avoid naming your variables as a reserved word in python (for example, "input" or "print").

# Band Naming Project #
# Check out the "project.py" file in the directory to see the project.

# That was the end of the first day! Congratulations!