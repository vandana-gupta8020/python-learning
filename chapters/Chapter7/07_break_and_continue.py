# THE BREAK STATEMENT
"""'break' is used to come out of the loop when encountered. It instructs the program to-exit the loop now.
"""

for i in range(100):
    if(i == 34):
        break         # Exit the loop right now
    print(i)
    

    
for i in range (0,80):
    print(i)
    if(i ==3):                    # this will print 0,1,2 and 3
        break
    


# THE CONTINUE STATEMENT
"""'continue' is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to "skip this iteration".
Example:"""
    
for i in range(100):
    if(i == 34):
        continue         # skip the iteration, Here iteration means value of 'i'. such as i = 0,1 3 56 78 ...
    print(i)


for i in range(4):
    print("printing")
    if i ==2:
        continue             # if i is 2, the iteration is skipped
    print(i)