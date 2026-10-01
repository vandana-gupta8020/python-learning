# Ques4:- Write a python program to print the contents of a directory using OS module. Search online for the function which does that.

import os

# Specify the directory you want to list (make sure this folder exists)
directory_path = 'C:\\Users\\CE00161624\\Desktop'

# List all files and directories in the specified path
try:
    contents = os.listdir(directory_path)

    # Print each file and directory name
    for item in contents:  # Fixed indentation
        print(item)

except FileNotFoundError as e:
    print(f"Error: {e}")
