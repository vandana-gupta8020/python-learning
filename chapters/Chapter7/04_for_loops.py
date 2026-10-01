# FOR LOOP
"""A for loop is used to iterate through a sequence like list, tuple, or string [iterables]
Syntax:"""

l= [1, 7, 8]

for item in l:
    print(item)       # prints: 1, 7 and 8
 

# RANGE FUNCTION IN PYTHON
"""
- The range() function in python is used to generate a sequence of number.
- We can also specify the start, stop and step-size as follows:
"""
"""range(start, stop, step_size)"""       #step size is usually not used with range()

# AN EXAMPLE DEMONSTRATING RANGE () FUNCTION.

for i in range(0,7):    # range(7) can also be used.
    print(1)            # prints: 0 to 6

for i in range(4):
    print(i)
    
    
for i in range(0, 100, 4):
    print(i)

