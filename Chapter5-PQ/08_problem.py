# 8. If languages of two friends are same; what will happen to the program in problem 6?

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

# Output:

"""
Enter friend name: Shivam   
Enter language: python
Enter friend name: Ravi
Enter language: JS
Enter friend name: Vandana
Enter language: Md
Enter friend name: Jyoti 
Enter language: Md
{'Shivam': 'python', 'Ravi': 'JS', 'Vandana': 'Md', 'Jyoti': 'Md'}
"""


# Note: If languages of two friends are same, all changes are reflecting same as per changes.
