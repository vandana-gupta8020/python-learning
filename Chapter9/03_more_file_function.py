"""
The random-access memory(RAM) is 'volatile', and all its contents are lost once a program terminates in order to persist the data forever, we use files.

A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.


There are 2 types of files:
1. Text files (.txt, .c etc)
2. Binary files (.jpg, .dat, etc)
- Python has a lot of functions for reading, updating, and deleting files.


=> OPENING A FILE
Python has an open () function for opening files. It takes 2 parameters: filename and mode.
"""



# open the text file
f = open("file.txt")
# f.readlines() function to read the lines
lines = f.readlines()
# prints the list of lines & their data type
print(lines, type(lines))
# close the file
f.close()


# ------------------------------------------ OR ------------------------


# Open the file in read mode
f = open("file.txt")
# Read the 1st line from the file and print its content and type
line1 = f.readline()
print(line1, type(line1))

# Read the 2nd line from the file and print its content and type
line2 = f.readline()
print(line2, type(line2))

# Read the 3rd line from the file and print its content and type
line3 = f.readline()
print(line3, type(line3))

# Read the 4th line from the file and print its content and type
line4 = f.readline()
print(line4, type(line4))

# Read the 5th line from the file and check if it is empty
line5 = f.readline()
print(line5 =="")        # True if 5th line is empty (i.e., end of file reached)


# Close the file to free up system resources
f.close()



# ------------------------------------------ OR ------------------------

# 🔁 Method 3: Using with and for Loop

with open("file.txt") as f:
    for i in range(4):
        line = f.readline()
        print(line, type(line))
       
       
# ------------------------------------------ OR ------------------------
# 🔁 Method 4: Loop Until End of file
# Open the file in read mode
f = open("file.txt")    
line = f.readline()       # Read until EOF using a while loop
while(line != ""):
    print(line)
    line = f.readline()
    
f.close()      # Close the file

"""
✅ What is EOF?
- EOF stands for 'End Of File'.
- In Python, when reading from a file using readline() or similar methods, it returns an empty string ("") when it reaches the end of the file.

🔍 Example:


f = open("file.txt")

line = f.readline()
while line != "":  # This checks for EOF
    print(line)
    line = f.readline()

f.close()

- Each time f.readline() is called, it reads the next line.

- When no more lines are left, it returns "", which means EOF.

"""
