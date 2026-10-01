# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks1 = int(input("enter the marks1: "))
marks2 = int(input("enter the marks2: "))
marks3 = int(input("enter the marks3: "))


# check total_percentage and marks

total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed!", total_percentage)
    
else:
    print("You failed! Please try again next year.", total_percentage)
    
    
  
marks1 = int(input("Enter your marks1:"))
marks2 = int(input("Enter your marks2:"))
marks3 = int(input("Enter your marks3:"))
marks4 = int(input("Enter your marks4:"))
marks5 = int(input("Enter your marks5:"))

# calculate toatl percentage
total_percentage = (100*(marks1+marks2+marks3+marks4+marks5)/500)

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33 and marks5>=33):
  print("You are passed!", total_percentage)
  
else:
  print("You failed! Try next time.", total_percentage)

