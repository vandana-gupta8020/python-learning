# 7. Write a program to find out whether a given post is talking about "Harry" or not.


# prompt the user enters the post
post = input("Enter the post: ")

# check if 'Harry' is mentioned in the post
if("Harry" in post):
    print("The post talks about Harry:", post)
    
else:
    print("The post doesn't talk about Harry:", post)
    
    
    
    
    
#-----------------------------------------------OR------------------------------------------------------

# prompt the user enters the post
post = input("Enter the post: ")

# check if 'harry' is mentioned in the post (case-insensitive)
if("Harry".lower() in post.lower()):
    print("The post talks about Harry:", post)
    
else:
    print("The post doesn't talk about Harry:", post)