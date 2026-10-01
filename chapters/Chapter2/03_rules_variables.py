# Variable Names:-
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

a = 23

aaa = 435

sameer = 4435

_sameer = 35

# @sameer = 45   # Invalid due to @ symbol

# s@meer  # Invalid due to @ symbol

"""Rules for defining a variable name (Also applies to other identifiers):-
- A variable name can contain alphabets(a-z), digits(0-9), and underscores.
- A variable name can only start with an alphabet and underscores.
- A variable name can't start with a digit.
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- No while space is allowed to be used inside a variable name.
Examples of a few variable names are: harry, one8, seven, _seven etc."""

"""Case-Sensitive
Variable names are case-sensitive.

Example
This will create two variables:"""

a = 4
A = "Sally"      # A will not overwrite a. It consider both values differ from each other.

print(a)
print(A)


myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

"""2myvar = "John"
my-var = "John"
my var = "John" #These example will produce an error in the result
"""

"""Multi Words Variable Names
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:"""

# Camel Case
# Each word, except the first, starts with a capital letter:

myVariableName = "vandanaGupta"
print(myVariableName)

# Pascal Case
# Each word starts with a capital letter:

MyVariableName = "VandanaGupta"
print(MyVariableName)

# Snake Case
# Each word is separated by an underscore character:

my_variable_name = "vandana_gupta"
print(my_variable_name)


"""Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:"""

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)      # Note: Make sure the number of variables matches the number of values, or else you will get an error.

"""One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:"""

x = y = z = "Orange"
print(x)
print(y)
print(z)


"""Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
"""
# Note:- Tuple ek immutable (change na hone wala) ordered collection hota hai Python me. Ye list ki tarah hota hai, lekin isme ek baar values assign ho jaayein, toh unko modify nahi kar sakte.


# Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

"""Output Variables
The Python print() function is often used to output variables.
"""
x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


# You can also use the + operator to output multiple variables:

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)              #  Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".


# For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)


# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error i.e unsupported operand type(s) for +: 'int' and 'str' :

"""
x = 5
y = "John"
print(x + y)
"""

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

x = 5
y = "John"
print(x,y)

"""Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables. Global variables can be used by everyone, both inside of functions and outside.

Create a variable outside of a function, and use it inside the function"""

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

"""If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

Create a variable inside a function, with the same name as the global variable."""

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


"""The global Keyword:-
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function. To create a global variable inside a function, you can use the global keyword.

If you use the global keyword, the variable belongs to the global scope:"""

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# Also, use the global keyword if you want to change a global variable inside a function.


# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

