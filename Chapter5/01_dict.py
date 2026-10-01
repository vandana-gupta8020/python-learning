d = {}      # Empty Dictionary

# Dictionary & Sets
"""
Dictionary is a collection of key-value pairs.

syntax:
a = {
    "key": "value",
    "Vandana": "Gupta",
    "Marks": 89,
    list: [23, 45, 56, 67]
}

a["key"]      # prints   "value"
a["list"]     # prints    [23, 45, 56, 67]
"""

# PROPERTIES OF PYTHON DICTIONARIES
"""
1. It is unordered.
2. It is mutable.
3. It is indexed.
4. It Cannot contain duplicate keys.
"""

marks = {
    "Jyoti": 78,
    "Preeti": 89,
    "Deepak": 88,
    "Kartik": 76 
}

print(marks, type(marks))                # output: {'Jyoti': 78, 'Preeti': 89, 'Deepak': 88, 'Kartik': 76} <class 'dict'>
print(marks["Preeti"])                # output: 89
print(marks["Preeti"], marks["Kartik"])                # output: 89 76
# Or 
# use a one-liner with a loop (still short and clean).This way, you access multiple keys in a single line — clean and compact.:
print(*[marks[name] for name in ["Preeti", "Kartik", "Jyoti"]])     # output: 89 76 78


# print(marks["Preeti", "Kartik"])  # Error: unhashable type, Because marks is a dictionary, and keys must be accessed one at a time — not as a group.