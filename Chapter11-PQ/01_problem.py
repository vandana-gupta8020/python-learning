# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.


# Create a class to represent a 2-D (two-dimensional) vector
class TwoDVector:
    
    # Constructor to initialize the vector components (i and j)
    def __init__(self, i, j):
        self.i = i  # Represents the i-component (like x-direction)
        self.j = j  # Represents the j-component (like y-direction)

    # Method to display the 2D vector in a readable format
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")
    
# Create a subclass for 3-D (three-dimensional) vector that inherits from TwoDVector
class ThreeDVector(TwoDVector):
    
    # Constructor to initialize i, j, and new k component
    def __init__(self, i, j, k):
        super().__init__(i, j)  # Call parent (2D) class constructor to set i and j
        self.k = k  # Add k-component (like z-direction) for 3D vector
        
    # Method to display the 3D vector
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")    


# Create an object of 2D vector with values i=1 and j=2
object1 = TwoDVector(1, 2)
object1.show()  # Output: The vector is 1i + 2j

# Create an object of 3D vector with values i=4, j=2, and k=3
object2 = ThreeDVector(4, 2, 3)
object2.show()  # Output: The vector is 4i + 2j + 3k

"""
🔍 Key Concepts Explained:-
Class: A blueprint to create objects (like vector).
Constructor __init__: Automatically called when object is created; sets initial values.
Inheritance (super()): Allows one class (3D) to reuse code from another class (2D).
show() Method: A function inside the class to display the vector nicely.
"""