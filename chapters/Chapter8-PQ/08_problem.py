# 8. Write a python function to print multiplication table of a given number.

# Define function that takes a number 'n'
def multiply(n):
    for i in range(1, 11):           # Define function that takes a number 'n'
        print(f"{n} X {i} = {n*i}")           # Print each line in the format: n X i = result
        
multiply(12)               # Call the function with number 5 to print its table



#--------------------------------------------------OR------------------------------------------------------

num = int(input("Enter a number: "))
def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = i{n*i}")



multiply(num)