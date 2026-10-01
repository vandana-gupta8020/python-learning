# FUNCTIONS & RECURSIONS
"""
- A function is a group of statements performing a specific task..
- When a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code is doing what!
- A function can be reused by the programmer in a given program any number of
EXAMPLE AND SYNTAX OF A FUNCTION
The syntax of a function looks as follows:"""

def func1():
    print('hello')     # This function can be called any number of times, anywhere in the program.
func1()



def greet():
    print("Hello Vandana")

greet()
# FUNCTION CALL
"""Whenever we want to call a function, we put the name of the function followed by parentheses as follows:
Func()
"""
# FUNCTION DEFINITION
"""
- The part containing the exact set of instructions which are executed during the function call."""

# Quick Quiz: Write a program to greet a user with "Good day" using functions.

# TYPES OF FUNCTIONS IN PYTHON
"""There are two types of functions in python:
- Built in functions (Already present in python).
Examples of built in functions includes len(), print(), range() etc.
- User defined functions (Defined by the user):
The func1() function we defined is an example of user defined function.
"""

# a = 34
# b = 23
# c = 25

# average = (a+b+c)/3
# print(average)

# x = 34
# y = 23
# z = 25

# average = (x+y+z)/3
# print(average)

# x = int(input("Enter your name: "))
# y = int(input("Enter your name: "))
# z = int(input("Enter your name: "))

# average = (x+y+z)/3
# print(average)

# a = int(input("Enter your name: "))
# b = int(input("Enter your name: "))
# c = int(input("Enter your name: "))

# average = (a+b+c)/3
# print(average)


# Function definition
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a+b+c)/3
    print(average)
avg()  # Function call
avg()
avg()