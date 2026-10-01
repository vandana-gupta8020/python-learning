# <--LISTS AND TUPLES-->
# Python lists are containers to store a set of values of any data type.
"""friends= ["apple", "akash","rohan",7,false]
1. str()
2. can store value of any datatype
3. int() bool()
5. boolean()"""

friends = ["Apple", "Orange", 5, 34.32, False, "Preeti", "Jyoti"]

print(friends[0])
print(friends[4])

friends[1] = "Grapes"         # Unlikes strings, Lists are mutable
print(friends[1])

print(friends[1:4])          #  list slicing


# LIST INDEXING
# A list can be indexed just like a string.       Note: index always starts from 0.

L1 = [7,9, "jyoti"]

print(L1[0])            # Output: 7
print(L1[1])            # Output: 9
print(L1[70])           # Output: error
print(L1[0:2])          # Output: [7,9]     # list slicing.

