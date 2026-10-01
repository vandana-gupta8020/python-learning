# 3. A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

phase1 = "Make a lot of money" 
phase2 = "buy now" 
phase3 = "subscribe this" 
phase4 = "click this"

message = input("Enter your comment: ")

if((phase1 in message) or (phase2 in message) or (phase3 in message) or (phase4 in message)):
    print("This comment is spam!")
    
else:
    print("This comment isn't a spam")