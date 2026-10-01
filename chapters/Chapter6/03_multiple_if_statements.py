

a = int(input("Enter your age: "))
# if statement no. 1
if(a%2 == 0):
    print("a is Even")
# End of if statement no. 1    
    
# if statement no. 2
if(a>=18):
    print("You are above the age of Consent")
    print("Good for you")
    
elif(a<0):
    print("You are entering invalid negative age.")
    
elif(a==0):
    print("You are entering 0, which is not valid age.")        
    
else:
    print("You are below the age of Consent")
# End of if statement no. 2   
    
print("End of Program")