s = {1, 3, 5, 56, 46, 5, 36, 36, 465, "Vandana", True}   # Note : True and 1 is considered the same value:

print(s, type(s))

# PROPERTIES OF SETS
"""
1. Sets are unordered => Element's order doesn't matter
2. Sets are unindexed => Cannot access elements by index
3. There is no way to change items in sets.
4. Sets cannot contain duplicate values."""

# OPERATIONS ON SETS
# Consider the following set:

s1={1,8,2,3}

"""len(s): Returns 4, the length of the set
s.remove(8): Updates the set s and removes 8 from s.
s.pop(): Removes an arbitrary element from the set and return the clement removed. I
s.clear():empties the set s.
s.union((8,113): Returns a new set with all items from both sets. (1,8,2,3,11).
s.intersection({8,11)): Return a set which contains only item in both sets (8)"""

s.remove(465)
print(s, type(s))    # Output: {1, 3, 36, 5, 46, 'Vandana', 56} <class 'set'>

s.clear()
print(s)       # output : set()

# the most used set methods in Python — especially useful in real-world coding and interviews:

# ✅ 1. add() : Adds a single element to the set.
my_set = {1, 2, 3}
my_set.add(10)
print("After add():", my_set)       # output : After add(): {10, 1, 2, 3}

# ✅ 2. update() : Adds multiple elements (from list, tuple, etc.) to the set.
my_set = {1, 2, 3}
my_set.update([11, 12, 13])
print("After update():", my_set)       # output : After update(): {1, 2, 3, 11, 12, 13}

# ✅ 3. remove() : Removes a specific item. Raises error if not found.
my_set = {10, 20, 30}
my_set.remove(10)
print("After remove():", my_set)       # output : After remove(): {20, 30}

# ✅ 4. discard() : Removes item without error if it doesn't exist.
my_set = {100, 200}
my_set.discard(300)  # No error even if 300 not present
print("After discard():", my_set)       # output : After discard(): {200, 100}

# ✅ 5. pop() : Removes and returns a random item.

my_set = {5, 6, 7}
item = my_set.pop()
print("Popped item:", item)       # output : Popped item: 5
print("After pop():", my_set)       # output : After pop(): {6, 7}

# ✅ 6. clear() : Removes all items from the set.
my_set = {1, 2, 3}
my_set.clear()
print("After clear():", my_set)       # output : After clear(): set()

# ✅ 7. union() : Returns a new set with all unique elements from both sets.
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a.union(b))       # output : Union: {1, 2, 3, 4, 5}

# ✅ 8. intersection() : Returns only the common elements.
a = {1, 2, 3}
b = {2, 3, 4}
print("Intersection:", a.intersection(b))       # output : Intersection: {2, 3}

# ✅ 9. difference() : Returns items in one set but not in the other.
a = {1, 2, 3}
b = {2, 3}
print("Difference (a - b):", a.difference(b))       # output : Difference (a - b): {1}

# ✅ 10. issubset() / issuperset() : Checks subset/superset relationships.
a = {1, 2}
b = {1, 2, 3}
print("Is a subset of b?:", a.issubset(b))       # output : Is a subset of b?: True
print("Is b a superset of a?:", b.issuperset(a))       # output : Is b a superset of a?: True

# These methods are powerful for:
"""
- Filtering data
- Removing duplicates
- Comparing groups
- Optimizing performance over lists
- Want a simple project using sets (like comparing student subjects)?
"""

# ✅ 11. symmetric_difference() : Returns elements that are in either set but not both (like XOR).

a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))  # Output: {1, 2, 4, 5}

# ✅ 12. intersection_update() : Keeps only the items found in both sets, modifies original set.
a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)
print(a)  # Output: {2, 3}

# ✅ 13. difference_update() : Removes the items found in another set from the current set.
a = {1, 2, 3}
b = {2, 3}
a.difference_update(b)
print(a)  # Output: {1}

# ✅ 14. symmetric_difference_update() : Updates the original set with the symmetric difference (XOR).
a = {1, 2}
b = {2, 3}
a.symmetric_difference_update(b)
print(a)  # Output: {1, 3}

# ✅ 15. copy() : Makes a shallow copy of the set.
a = {1, 2, 3}
b = a.copy()

# ✅ 16. isdisjoint(): Returns True if two sets have no common element : .
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # Output: True


# Summary of Real Use Cases:
"""
| 'Method'	          | 'Use Case'               |
| union()	          | Combine unique items     |
| intersection()	  | Find common elements     |
| difference()	      | Filter out items         |
| isdisjoint()	      | Check no overlap         |
| update()	          | Add many elements        |
"""


