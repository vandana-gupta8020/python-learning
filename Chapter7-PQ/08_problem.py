# 8. Write a program to print the following star pattern: (Left-Aligned Triangle)
"""
for n = 3

*
**
*** 

"""
# Prompt the user to enter a number
n = int(input("Enter your number: "))

# Loop from 1 to n (inclusive).This loop runs from 1 to n, inclusive. Each iteration represents a row in the pattern.
for i in range(1, n+1):
# Print 'i' number of asterisks '*' on the same line    
    print("*"* i, end="")
# Move to the next line after printing asterisks
    print("")
    
