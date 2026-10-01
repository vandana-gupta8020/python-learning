# OPERATORS IN PYTHON

"""Following are some common operators in python:
1. Arithmetic operators: +,-,^, / etc.
2. Assignment operators: =, +=, -= etc.
3. Comparison operators: ==, >, >=, <, != etc.
4. Logical operators: and, or, not."""


# 1. Arithmetic operators: +,-,^, / etc.
a = 2
b = 5
c = a + b 

print(c)

# 2. Assignment Operators: =, +=, -= etc.

a = 4-2 # Assign 4-2 in a
print(a)

b = 6
b += 3 # Increment the value of b by 3 and then assign it to b.
print(b)

c = 5
c *= 2   # Twice the value of c and then assign it to c.
print(c)

d = 5
d *= 3   # Thrice the value of d and then assign it to d.
print(d)

# 3. Comparison operators: ==, >, >=, <, != etc. Its output always be boolean.

d = 5<4
print(d)

d = 5>4
print(d)

d = 5!=4          # here, while != means to not equal to.
print(d)

d = 5==4         # here, while double equal to(==) is a comparison operator, while single equal to(=) assignment opertor.
print(d)


# 4. Logical operators: and, or, not.


# truth table of 'or'
e = True or False
print("True or False is", True or False)          # output: True or False is True
print("True or True is", True or True)            # output: True or True is True
print("False or True is", False or True)          # output: False or True is True
print("False or False is", False or False)        # output: False or False is False


# truth table of 'and'
print("True and False is", True and False)        # output: True and False is False
print("True and True is", True and True)          # output: True and True is True
print("False and True is", False and True)        # output: False and True is False
print("False and False is", False and False)      # output: False and False is False


# truth table of 'not'

print(not(True))                                  # output: False

print(not(False))                                  # output: True