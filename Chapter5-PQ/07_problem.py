# 7. If the names of 2 friends are same; what will happen to the program in problem 6?

d = {}

name = input("Enter friend name: ")
lang = input("Enter language: ")
d.update({name:lang})

name = input("Enter friend name: ")
lang = input("Enter language: ")
d.update({name:lang})

name = input("Enter friend name: ")
lang = input("Enter language: ")
d.update({name:lang})

name = input("Enter friend name: ")
lang = input("Enter language: ")
d.update({name:lang})

print(d)

# Output :
"""
    Enter friend name: Shivani
Enter language: Hindi
Enter friend name: Pinki
Enter language: English
Enter friend name: Shivani
Enter language: Urdu
Enter friend name: Nisha
Enter language: german
{'Shivani': 'Urdu', 'Pinki': 'English', 'Nisha': 'german'}
"""

# note: If the 2 friends name are same, then dictionary consider only one which were last updated.