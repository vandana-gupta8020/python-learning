# 6. Write a program to mine a log file and find out whether it contains 'Python'.

with open("06_log.txt") as f:
    content = f.read()
    
if("Python" in content):
    print("Yes! Python is present.")
    
else:
    (print("No! Python is not present"))