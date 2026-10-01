# 6. Create an empty dictionary. Allow 4 name to enter their favorite language as value and use key as their names. Assume that the names are unique.

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


#----------------------------------------------------------------------- OR---------------------------------------------------------------------#

d = {}

d["Shivam"] = input("Shivam's favourite language: ")
d["Kashish"] = input("Kashish's favourite language: ")
d["Ravi"] = input("Ravi's favourite language: ")
d["Vishal"] = input("Vishal's favourite language: ")

print(d)
