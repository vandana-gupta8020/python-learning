# TUPLE METHODS
"""Consider the following tuple.tuple
a = (1,7, 2)
a.count(1): a count (1) will return number of times 1 occurs in a.
a.index(1) will return the index of first occurrence of 1 in a.
"""

# Tuples in Python are immutable, meaning their values cannot be changed after creation. However, there are a few useful methods that can be used with tuples.

# Common Tuple Methods in Python:
    
# count(value) – Returns the number of times a specified value appears in the tuple.
my_tuple = (1, 2, 2, 3, 4, 2)
print(my_tuple.count(2))                   # Output: 3

# index(value, start, end) – Returns the index of the first occurrence of the specified value.

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple.index(30))                   # Output: 2

# len(tuple) – Returns the total number of elements in the tuple.

my_tuple = (5, 10, 15)
print(len(my_tuple))                   # Output: 3

# max(tuple) – Returns the maximum value in the tuple (works with numbers or strings).


my_tuple = (10, 50, 20, 80)
print(max(my_tuple))                   # Output: 80

# min(tuple) – Returns the minimum value in the tuple.


my_tuple = (5, 25, 15, 40)
print(min(my_tuple))                   # Output: 5

# sum(tuple) – Returns the sum of all elements in a numeric tuple.


my_tuple = (1, 2, 3, 4)
print(sum(my_tuple))                   # Output: 10

# sorted(tuple) – Returns a sorted list from the tuple (does not modify the tuple itself).

my_tuple = (3, 1, 4, 2)
print(sorted(my_tuple))                   # Output: [1, 2, 3, 4]

# tuple(iterable) – Converts an iterable (like a list) into a tuple.

my_list = [10, 20, 30]
my_tuple = tuple(my_list)
print(my_tuple)                   # Output: (10, 20, 30)

# 📌Note:- Since tuples are immutable, they do not support methods like append(), remove(), or pop(), which are available for lists. Let me know if you need more details! 😊

a = (2, 445, 563, 563, False, "Vandana", "Jyoti")
print(a)
no = a.count(563)
print(no)
print(a.count("Vandana"))

i = a.index(2)
print(i)

b = (455, 345, 576, 4450, True, "Deepak")
print(len(b))

"""Operations with Tuples in Python"""

# Tuples in Python are immutable, meaning you cannot modify them directly (like adding or removing elements). However, you can perform various operations on tuples.

# 1️⃣ Concatenation (+ Operator): You can join two tuples using the + operator.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4, 5, 6)

# 2️⃣ Repetition (* Operator): You can repeat a tuple multiple times using *.
tuple1 = (10, 20)
result = tuple1 * 3
print(result)  # Output: (10, 20, 10, 20, 10, 20)

# 3️⃣ Membership (in and not in): You can check if an element exists in a tuple.
tuple1 = (1, 2, 3, 4, 5)
print(3 in tuple1)   # Output: True
print(10 not in tuple1)  # Output: True

# 4️⃣ Iteration (Using for Loop): You can loop through a tuple using a for loop.
tuple1 = ("apple", "banana", "cherry")
for item in tuple1:
    print(item)                 # Output: apple banana cherry

  
# 5️⃣ Slicing Tuples ([:] Operator): You can extract a portion of a tuple using slicing.
tuple1 = (0, 1, 2, 3, 4, 5, 6)
print(tuple1[1:4])   # Output: (1, 2, 3)
print(tuple1[:3])    # Output: (0, 1, 2)
print(tuple1[2:])    # Output: (2, 3, 4, 5, 6)
print(tuple1[-3:])   # Output: (4, 5, 6)

# 6️⃣ Tuple Unpacking: You can assign tuple elements to variables directly.
tuple1 = ("John", 25, "Developer")
name, age, job = tuple1
print(name)  # Output: John
print(age)   # Output: 25
print(job)   # Output: Developer

# 7️⃣ Finding Length (len()): You can find the number of elements in a tuple using len().
tuple1 = (1, 2, 3, 4, 5)
print(len(tuple1))  # Output: 5

# 8️⃣ Finding Maximum & Minimum (max(), min()): These functions return the highest and lowest values in a tuple.
tuple1 = (10, 5, 30, 20)
print(max(tuple1))  # Output: 30
print(min(tuple1))  # Output: 5

# 9️⃣ Counting Elements (count()): Find how many times a value appears in a tuple.
tuple1 = (1, 2, 3, 2, 2, 4)
print(tuple1.count(2))  # Output: 3

# 🔟 Finding Index (index()): Find the index of a value in a tuple.
tuple1 = (10, 20, 30, 40, 20)
print(tuple1.index(20))  # Output: 1 (first occurrence)

# 6️⃣ Length (len()) → Tuple ke elements count karne ke liye

my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))  # Output: 5

# 📌 Note: Since tuples are immutable, you cannot modify them (like adding, removing, or updating elements). If you need to modify a tuple, you must convert it into a list first, make changes, and then convert it back to a tuple.


