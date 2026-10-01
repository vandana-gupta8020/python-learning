# 4. Write a program to find whether a given number is prime or not.

n = int(input("Enter a no.: "))

for i in range(2, n):
    if(n%i) == 0:
        print("Its number is not prime")
        break
    
else:
    print("Number is prime")