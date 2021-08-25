# Welcome to the 2nd day of python programming!
# Today, we are going to learn about "Data types" and "String manipulation"
# We are also going to create a "Tip Calculator"

# Yesterday, we saw the "len()" function to get the number of characters in a string.
print(len('Hello World!')) # This will print "12" as there are 12 characters in "Hello World!"
# Now, instead of a string, we can pass a number into the "len()" function and we want to know how many digits are in that number.
# print(len(1234)) # If we remove the first "# " in this sentence and run it, you wlll see that we got a "TypeError" that an "int has no len()"
# To understand what this means, we have to learn about "Data Types".

# Data Types.
# On Day 1, we understood a data type called "Strings", but there are many more data types out there.
# Today, we are going to learn about some of the common and important data types.

# Now, we are going to see how to get a specific character in a string.
# If we add an "[]" after the string, and specify which character "index" we want to get, we can get the character.
print("Hello"[0]) # This will print "H" as the first character in "Hello" is "H"
# Note that the first index starts at 0, not 1.

# To get the last character in a string, we can either count the number of characters in the string from "0" and change the number in the [] brackets to that index.
print("Hello"[4]) # This will print "o" as the 4th index (5th character) in "Hello" is "o"
# We can also use negative numbers to get the last character in a string.
print("Hello"[-1]) # This will print "o" as the last character in "Hello" is "o"

print('123' + '456') # This will print out "123456" as '123 and '456' are both strings.
# We are just concatenating the strings together, instead of adding them as number.

# To add them, we have to use a different data type.
# We use the data type "integer" in python as "numbers".

# Integers
# Integers are numbers without any decimals. Thus, they are like "whole numbers"
# To declare an integer, you just have to type that "number".
print(123) # This will print "123" as an integer
print(123 + 456) # Now, we write the above 123 + 456, as integers, we get "579" which is the sum of the two integers.

# Floats
# Floats are numbers with decimals.
# This is also known as "Floating point numbers"
print(1.23) # This will print "1.23" as a float

# Boolean
# Booleans are either "True" or "False"
# We use "True" and "False" to represent "yes" and "no"
# The "True" and "False" always begins with a capital "T" and "F" and are always in the same case.
print(True) # This will print "True" as a boolean

# Previosuly we saw how the "len()" function gives us a "TypeError" when we pass in a number.
# Also, if we try to add a string and an integer, we get a "TypeError" as well.
# print('Hello' + 6) # This will give us a "TypeError" saying that "You can't concatenate a string and an int"

# The "type()" function.
# This function tells us what type of data we are passing into the function.
print(type(123)) # This will print "int" as we are passing in an integer.

# Type Conversion.
# To convert an "integer" into a "string", we use the "str()" function.
print(str(123)) # This will print "123" as a string, instead of an integer as we are converting the integer into a string using the "str()" function.

# We can also convert other data types into other types too using their respective function.
print(int('123')) # This will print "123" as an integer, as we use the "int()" function.
print(float(123)) # This will print "123.0" as a float, as we use the "float()" function.