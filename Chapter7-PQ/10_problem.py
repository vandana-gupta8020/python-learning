# 10. Write a program to print multiplication table of n using for loops in order. 5x1=5, 5x2=10, 5x3=15.....

# prompt the user to enter a number
n = int(input("Enter your number: "))

# loop from 10 down to 1
for i in range(1, 11):
    # print the multiplication result
    print(f"{n} X {i} = {n*i}")
    
    
# 11. Write a program to print multiplication table of n using for loops in reversed order.5x10=50, 5x9=45, 5x8=40.....

# prompt the user to enter a number
n = int(input("Enter your number: "))

# loop from 1 to 10
for i in range(1, 11):
    # print the multiplication result
    print(f"{n} X {11-i} = {n*(11-i)}")