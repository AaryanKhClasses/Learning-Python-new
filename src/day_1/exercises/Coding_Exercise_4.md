# Variables Exercise
## In this exercise, you have to work with variables.

# Instructions:
### You have to exchange the values of two variables and print them.
### Also, the code should work for any input.
### **HINT:** You can make use of a third or potentially a fourth variable to do this.

# Solution
### I recommend you **NOT** to see this before you solve this exercise.
### If you have completed this and got the result as expects **OR** you got stuck somewhere. You can see this!
<details>
    <summary>Click to show the code</summary>

```py
# The values of the variables in the question
a = input('Enter the value of "a": ')
b = input('Enter the value of "b": ')

temp = a # Store the value of a in a temporary variable
a = b # Now assign b to a
b = temp # Now assign temp ("a", before the value of "a" changed) to b
print('The value of a is now ' + a + ' and the value of b is now ' +  b) # Print the values of a and b
```
</details>