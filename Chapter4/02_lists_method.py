
# LIST METHODS.
# Consider the following list:

L1 = [1,8,7,2,21,15]

"""
L1.sort(): updates the list to [1,2,7,8,15,211
L1.reverse(): updates the list to [15.21.2.7.8.1]
L1.append(8): adds 8 at the end of the list
L1.insert(3,8): This will add 8 at 3 index
L1.pop(2): Will delete element at index 2 and return its value.
L1.remove(21): Will remove 21 from the list.
"""

# list_name.append() -  method

friends = ["Apple", "Orange", 5, 34.32, False, "Preeti", "Jyoti"]
print(friends)

friends.append("Deepak")
# friends.append("Deepak", "Ravi")          friends.append() method in Python only allows adding a single element at a time. If you try to pass multiple elements, it will cause an error.
print(friends)


# If you pass a list inside append(), it will treat it as a single element, creating a nested list.
numbers = [1, 2, 3]
numbers.append([4, 5])  # Adds the entire list as one element           ----> Using append() with a list (Nested List)
print(numbers)


class6th = ["Ravi", "Jyoti", "Deepak", "Preeti"]
class6th.append(["Vandana", "Khushi"])
print(class6th)                                                    #   ----> Using append() with a list (Nested List)

# TUPLES IN PYTHON
# A tuple is an immutable data type in python.

a = ()          # empty tuple
a = (1,)        # tuple with only one element needs a comma
a = (1,7,2)     # tuple with more than one element

# TUPLE METHODS
# - Consider the following tuple:


# Sorting list 
l1 = [1,8,7,2,21,15]
l1.sort()
print(l1)                  # Output:- [1, 2, 7, 8, 15, 21]

# Reversing list
l1.reverse()
print(l1)                  # Output:- [21, 15, 8, 7, 2, 1]

# insertion list
l1 = [1,8,7,2,21,15]

l1.insert(3,23.5)             #  This will add 23.5 at 3 index
print(l1)                     # Output :- [1, 8, 7, 23.5, 2, 21, 15]

l1 = [1,8,7,2,21,15]
l1.pop(4)
print(l1)

print(l1.pop(4))

#   OR
l1 = [1,8,7,2,21,15]
value = l1.pop(4)
print(value)
print

# Remove from list

l1 = [1,8,7,2,21,15, 45]
l1.remove(15)                    # remove 15 from the existing list.
print(l1)                        # Output:- [1, 8, 7, 2, 21, 45]


# comparison between list and tuple in Python:
"""
| Feature     |  List                      |    Tuple                           |

| Definition  |	A list is an ordered, changeable (mutable) collection of items in Python. We can add, remove, or modify elements in a list.	 |  A tuple is an ordered, but unchangeable (immutable) collection of items in Python. Once created, you cannot modify its elements.  |

| Syntax	  |  my_list = [1, 2, 3]	   |    my_tuple = (1, 2, 3)          |
| Mutable	  |  ✅Yes (you can change it) |   ❌ No (you cannot change it)  |
| Speed 	  |  Slower                    |	 Faster                       |
| Use case    |	 When data can change	   |     When data should not change  |
| Methods	  |  Has many (e.g. append(), pop())|	Fewer methods             |
"""
# List
my_list = [1, 2, 3]
my_list.append(4)  # ✅ allowed
print(type(my_list))

# Tuple
my_tuple = (1, 2, 3)
# my_tuple.append(4) ❌ Error: 'tuple' object has no attribute 'append'
print(type(my_tuple))