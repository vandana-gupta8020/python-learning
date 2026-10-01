# 1. Write a program to find the greatest of four numbers entered by the user.

a1 = int(input("Enter your no. 1: "))
a2 = int(input("Enter your no. 2: "))
a3 = int(input("Enter your no. 3: "))
a4 = int(input("Enter your no. 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("greatest no. is a1:", a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("greatest no. is a2:", a2)
elif(a3>a2 and a3>a1 and a3>a4):
    print("greatest no. is a3:", a3)
elif(a4>a2 and a4>a3 and a4>a1):
    print("greatest no. is a4:", a4)
