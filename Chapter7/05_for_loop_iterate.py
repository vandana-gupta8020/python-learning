## 🔹 What is 'i' in a 'for' loop?
"""
👉 i is just a temporary name used to pick each item one by one from a list, tuple, or string.
👉 i just holds one value at a time from the group you're looping through."""


## For loop with list
l = [1, 3, 4, 6, 234, 674, 6]
for i in l:
    print(i)
    
## For loop with tuple    
t = (4, 45, 455, 74, 76)
for i in t:
    print(i)
    
## For loop with string
s = "Vandana"
for i in s:
    print(i)


fruits = ["apple", "banana", "mango"]

# Now, we want to look at each fruit one at a time:
for i in fruits:
    print(i)
    
# This means:
"""
First, i becomes "apple" → it prints "apple".
Then, i becomes "banana" → it prints "banana".
Then, i becomes "mango" → it prints "mango"."""