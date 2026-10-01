# 7. Write a program to find out the line number where python is present from ques 6.

with open("06_log.txt") as f:
    lines = f.readlines()

lineNo = 1
for line in lines:
    if("Python" in line):
        print(f"Yes! Python is present. Line no is {lineNo}")
        break
    lineNo += 1
    
else:
    (print("No! Python is not present"))
        