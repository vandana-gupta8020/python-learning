# Python - Join Sets

# Join Sets
"""
There are several ways to join two or more sets in Python.
The union() and update() methods joins all items from both sets.
The intersection() method keeps ONLY the duplicates.
The difference() method keeps the items from the first set that are not in the other set(s).
The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""
# Union
"""
The union() method returns a new set with all items from both sets.
Example:- Join set1 and set2 into a new set:"""

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)             # Ouput:- {1, 2, 'b', 3, 'c', 'a'}

# Note:- You can use the | operator instead of the union() method, and you will get the same result.
"""
Example:- Use | to join two sets:
"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)             # Ouput:- {'b', 1, 2, 'c', 3, 'a'}

# Join Multiple Sets
"""
All the joining methods and operators can be used to join multiple sets.
When using a method, just add more sets in the parentheses, separated by commas:
Example:- Join multiple sets with the union() method:
"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)             # Ouput:- {'a', apple, 'c', cherry, 'b', banana, 3, Elena, 2, John, 1}

# Note:- When using the | operator, separate the sets with more | operators:
"""
Example:- Use | to join two sets:
"""

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)             # Ouput:- {apple, cherry, 'c', John, 1, 2, 3, 'b', 'a', banana, Elena}

# Join a Set and a Tuple
"""
The union() method allows you to join a set with other data types, like lists or tuples.
The result will be a set.
Example:- Join a set with a tuple:
"""
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)             # Ouput:- {1, 2, 3, 'b', 'a', 'c'}  Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

# Update
"""
The update() method inserts all items from one set into another.
The update() changes the original set, and does not return a new set.
Example:-The update() method inserts the items in set2 into set1:
"""
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)             # Ouput:- {'c', 'b', 1, 2, 3, 'a'}   Note: Both union() and update() will exclude any duplicate items.

# Intersection
"""
Keep ONLY the duplicates
The intersection() method will return a new set, that only contains the items that are present in both sets.
Example:- Join set1 and set2, but keep only the duplicates:
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)             # Ouput:- {'apple'}

# You can use the & operator instead of the intersection() method, and you will get the same result.
"""
Example:- Use & to join two sets:
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)             # Ouput:- {'apple'}    Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

"""
The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
Example:- Keep the items that exist in both set1, and set2:
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)             # Ouput:- {'apple'}

"""
The values True and 1 are considered the same value. The same goes for False and 0.
Example:- Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
"""
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)             # Ouput:- {False, True, 'apple'}

# Difference
"""
The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
Example:- Keep all items from set1 that are not in set2:
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)             # Ouput:- 
"""
You can use the - operator instead of the difference() method, and you will get the same result.
Example:- Use - to join two sets:
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)             # Ouput:-  Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

"""
The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
Example:- Use the difference_update() method to keep the items that are not present in both sets:
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)             # Ouput:- {'banana', 'cherry'}

# Symmetric Differences

"""
The symmetric_difference() method will keep only the elements that are NOT present in both sets.
Example:-Keep the items that are not present in both sets:
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)             # Ouput:- {'google', 'banana', 'microsoft', 'cherry'}

"""
You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
Example:- Use ^ to join two sets:
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)             # Ouput:- {'google', 'banana', 'microsoft', 'cherry'}  Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

"""
The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
Example:- Use the symmetric_difference_update() method to keep the items that are not present in both sets:
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)             # Ouput:- {'google', 'banana', 'microsoft', 'cherry'}


# The set() Constructor
"""
It is also possible to use the set() constructor to make a set.
Example:- Using the set() constructor to make a set:
"""

thisset = set(("apple", "banana", "cherry"))
print(thisset)             # Ouput:- {'banana', 'apple', 'cherry'}   Note: the set list is unordered, so the result will display the items in a random order.

