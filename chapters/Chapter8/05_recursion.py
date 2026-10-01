   
    
# RECURSION
"""
- Recursion is a function which calls itself.
- It is used to directly use a mathematical formula as function.
Example:
factorial(n) = n x factorial (n-1)
"""
# This function can be defined as follows:
"""
def factorial(n):
    if i == 0 or i==1: # base condition which doesn't call the function any further
        return 1
    else:
        return n*factorial (n-1) # function calling itself

"""

"""

factorial(0) OR 0! = 1
factorial(1) OR 1! = 1
factorial(2) OR 2! = 2 X 1
factorial(3) OR 3! = 3 X 2 X 1
factorial(4) OR 4! = 4 X 3 X 2 X 1
factorial(5) OR 5! = 5 X 4 X 3 X 2 X 1


factorial(n) OR n! = n X (n-1) X (n-2) X (n-3) X .....X 3 X 2 X 1

factorial(n) OR n! = n*factorial(n-1)
               OR
factorial(n) OR n! = n X (n-1)!

"""

# Ask user to enter a number and convert input string to integer
n = int(input("Enter a number: "))
# Define a recursive function to calculate factorial
def factorial(n):
    if(n==1 or n==0):     # base condition: stops recursion when n is 0 or 1
        return 1
    return n* factorial(n-1)          # recursive step: n * factorial of (n-1)

# Print the result of the factorial function
print(f"The factorial of this number is: {factorial(n)}")