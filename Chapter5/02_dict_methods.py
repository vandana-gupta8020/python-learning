# DICTIONARY METHODS
"""
Consider the following dictionary.

a = {
    "name":"harry"
    "from":"india"
    "marks": [92,98,96]
    }
"""

# Methods:-
"""
- a.items(): Returns a list of (key, value)tuples.
- a.keys(): Returns a list containing dictionary's keys.
- a.update({"friends":}): Updates the dictionary with supplied key-value pairs.
- a.get("name"): Returns the value of the specified keys (and value is returned eg."harry" is returned here).

More methods are available on docs.python.org
"""
marks = {
    "Jyoti": 78,
    "Preeti": 89,
    "Deepak": 88,
    "Kartik": 76 
}

print(marks, type(marks))

#🔹items() :- Returns the list of tuples (key-value pairs).
print(marks.items())     # dict_items([('Jyoti', 78), ('Preeti', 89), ('Deepak', 88), ('Kartik', 76)])

#🔹keys() :- Returns all the keys in the dictionary.
print(marks.keys())  # dict_keys(['Jyoti', 'Preeti', 'Deepak', 'Kartik'])

# 🔹 values() :- Returns all the values.
print(marks.values())  # dict_values([78, 89, 88, 76])

# 🔹 items() :- Returns key–value pairs as tuples.
print(marks.items())   # dict_items([('Jyoti', 78), ('Preeti', 89), ...])

# 🔹 get(key) :- Returns the value for the key (safer than marks[key]).
print(marks.get("Preeti"))  # 89
# 🔹 update() :- Adds or updates a key–value pair.
print(marks.update({"Preeti": 99, "Anjali": 90}))
# 🔹 pop(key) :- Removes the key and returns its value.
print(marks.pop("Deepak"))  # Removes 'Deepak'
# # 🔹 clear() :- Removes all items.
print(marks.clear())
# 🔹copy() :- Return a shallow copy of a dictionary.
print(marks.copy())

