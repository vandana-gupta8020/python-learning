"""TYPE() FUNCTION AND TYPECASTING:-

type() function is used to find the data type of a given variable in python.
       You can get the data type of a variable with the type() function.
"""

x = 5
y = "John"
z = False
w = 756.7
print(type(x))
print(type(y))
print(type(z))
print(type(w))

a = 31
t = type(a)                 # class <int>
print(t)

b = "31"
t = type(b)                # class <str>    note:- A number can be converted into a string and vice versa (if possible).
print(t)

# There are many functions to convert one data type into another.
c = "32.343"
t = type(c)
print(t)

c = "32.343"
d = float(c)               # 'c' is string but the type should be float.
t = type(d)
print(t)

"""str(31)   =>"31"        # integer to string conversion

int("32")    => 32         # string to integer conversion.

float(32)    => 32.02      # Integer to float conversion
... and so, on
Here "31" is a string literal and 31 a numeric literal."""
