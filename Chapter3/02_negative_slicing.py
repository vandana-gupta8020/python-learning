# Negative slicing starts from right to left(-1, -2, -3, -4,....) & positive slicing starts from left to right(o, 1, 2, 3, 4,....)

name = "Harry"

print(name[0:3])

print(name[-4 : -1])
print(name[1:4])       # is same as print(name[-4:-1])

# Other advanced slicing techniques
print(name[:4])        # is same as print(name[0:4])
print(name[1:])        # is same as print(name[1:5])
print(name[1:5])
print(name[0:5])


"""SLICING WITH 'SKIP VALUE':-
We can provide a skip value as a part of our slice like this:"""

word = "amazing"
word[1:6:2]

print(word)
print(word[1:6:2])               # Output:  mzn


# Note:- [start:stop:step] = [1:3:2]
"""Slicing Process:
Start at index 1 → "a".
Now, take every 2nd character from the substring formed by a[1:3], which is "an".
Since we are stepping by 2, the second character "n" is skipped.
So we end up with just "a".
"""

a = "Vandana"
a[1:3:2]
print(a[1:3:2])


b = "0123456789"
b[1:7:3]
print(b[1:7:3])


"""What is an Index?
- An index is just the position of a letter in a sentence, starting from 0.

For example:
H  E  L  L  O
0  1  2  3  4
👉 The letter 'H' is at index 0, 'E' at 1, and so on.
"""
