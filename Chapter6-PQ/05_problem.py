# 5. Write a program which finds out whether a given name is present in a list or not.

l = ["harry", "Tom", "Shivam", "Divya", "Jyoti"]

name = input("Enter your name: ")

if(name in l):
    print("this name is present in the given list", l)
    
else:
    print("Sorry! this is not present in the given list", l)