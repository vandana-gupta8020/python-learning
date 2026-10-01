# 4. Write a program to find whether a given username contains less than 10 characters or not.

# prompt the user to enter the username
username = input("Enter username: ")

# Check the length of username 
if (len(username)<10):
    print("Username contains less than 10 characters.", username)
    
else:
    print("username contains more than 10 characters.", username)