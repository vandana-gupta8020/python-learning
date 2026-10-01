# 2. Write a program to accept marks om 6 students and display them in a sorted manner.

marks = []

m1 = int(input("Enter marks of 1st Student: "))
marks.append(m1)
m2 = int(input("Enter marks of 2nd Student: "))
marks.append(m2)
m3 = int(input("Enter marks of 3rd Student: "))
marks.append(m3)
m4 = int(input("Enter marks of 4th Student: "))
marks.append(m4)
m5 = int(input("Enter marks of 5th Student: "))
marks.append(m5)
m6 = int(input("Enter marks of 6th Student: "))
marks.append(m6)

marks.sort()
print(marks)
