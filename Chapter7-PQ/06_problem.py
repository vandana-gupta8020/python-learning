
# 6. Write a program to calculate the factorial of a given number using for loop.

# factorial =>  5! = 1 x 2 x 3 x 4 x 5 = 120

n = int(input("Enter a number: "))         # Ask user for a number
product = 1                         # Start with 1 (because multiplying by 0 would always give 0)
for i in range(1, n+1):             # Loop from 1 to n
    product = product * i           # Multiply each number with the previous result
    
print(f"The factorial of {n} is {product}")

# Example:- If user enters 5, the loop does:
"""
product = 1 × 1 = 1

product = 1 × 2 = 2

product = 2 × 3 = 6

product = 6 × 4 = 24

product = 24 × 5 = 120

So the output is:   The factorial of 5 is 120
"""