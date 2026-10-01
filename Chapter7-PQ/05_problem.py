# 5. Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter natural number: "))            # Ask the user for a number

i = 1           # Start counting from 1
sum = 0         # Initial sum is 0

while(i<=n):            # Keep going until i reaches n
    sum += i            # Add i to the sum
    i += 1          # Move to the next number
    
print(sum)          # Print the final result
    
    
    