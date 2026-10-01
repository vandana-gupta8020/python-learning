# 5. Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.


from random import randint          # alternative way to import module instead of 'import random'
# import random    

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book(self, fro, to):
        print(f"The train is booked in train no. {self.trainNo} from {fro} to {to}.")
    
    
    def getStatus(self):
        print(f"The train {self.trainNo}: running on time.")
    
    
    def getFare(self, fro, to):
        print(f"Train fare of train no. {self.trainNo} from {fro} to {to} is {randint(250, 1000)}.")
        
indian_railway_train = Train(12598)
indian_railway_train.book("Delhi", "Agra")
indian_railway_train.getStatus()
indian_railway_train.getFare("Delhi", "Agra")