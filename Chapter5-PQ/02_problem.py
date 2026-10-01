# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).
s = set()
n = input("Enter no. 1: ")
s.add(int(n))
n = input("Enter no. 2: ")
s.add(int(n))
n = input("Enter no. 3: ")
s.add(int(n))
n = input("Enter no. 4: ")
s.add(int(n))
n = input("Enter no. 5: ")
s.add(int(n))
n = input("Enter no. 6: ")
s.add(int(n))
n = input("Enter no. 7: ")
s.add(int(n))
n = input("Enter no. 8: ")
s.add(int(n))

print(s)


#----------------------------------------------------------------------- OR---------------------------------------------------------------------#


# You can simplify it using a for loop to avoid repetition. Both versions are correct — yours is just longer but works perfectly.

s = set()

for i in range(1, 9):
    n = int(input(f"Enter number {i}: "))
    s.add(n)

print("Unique numbers:", s)


