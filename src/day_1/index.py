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
# print("Hello World!) # If you remove the first "#" in this line, you can see that the last parentesis is also colored! This means that the string has not ended there and will result in an error!
# If you run the code as-it-is without fixing the "string issue", its gonna give you an error in the console.
# We will get into the "Errors" in the future!

## An interactive Coding Exercise ##
# The coding exercise is given in this MD file: https://github.com/AaryanKhClasses/Learning-Python-new/tree/main/src/assets/Coding_Exercise_1.md
# I know thats a long hyperlink, but most code editors allows you to "Ctrl+Click" to follow that link!

# I hope you have completed the exercise sincerely. Now lets move on.

# While completing the exercise, you can see the third "print" statement was as follows:
print("print('what to print')") # Why have we put a "single" quote inside the print statement inside the string? Why have we not put a "double" quote?
# Thats because, in python. The interpreter doesn't really care how you close a string. A string can be written insid a "double" quote as well as a "single" quote!
# Now, if I replace the single quotes with double quotes: (after removing the first "#")
# print("print("what to print")") # It counts `print("print(` as one string and `")"` as a different one, completely excluding the middle part and the python think its actual code and trys to interpret it.
# But as its not valid code, python will give you an "error" if you try to run it!

# Now how to fix this?
# Commonly, you just replace the "double" quotes to "single" quotes or the other way around!
# But theres an another way to fix this which we will see afterwards!