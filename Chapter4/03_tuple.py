# TUPLES IN PYTHON
"""
- Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
- A tuple is a collection which is ordered and unchangeable.
- Tuples are written with round brackets.
"""

# A tuple is an immutable data type in python.
a = ()                       # empty tuple
a = (1,)                    # tuple with only one element needs a Comma
a = (1,7,2)                  # tuple with more than one element


a = (1, 2, 5, 6)
print(type(a))

b = ()
print(type(b))

c = (5,)
print(type(c))

d = (2, 445, 563, False, "Vandana", "Jyoti")
print(d)
print(type(d))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
print(thistuple[:4])
print(thistuple[2:5])

# Update Tuples:-

# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)      # output :- ('apple', 'kiwi', 'cherry')