# 2. Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. Add a method 'bark' to class 'Dog'.

# Base class representing general animals
class Animals:
    pass   # 'pass' means no properties or methods yet, it's just a placeholder

# 'Pets' class inherits from 'Animals'
class Pets(Animals):
    pass # This class can later have properties or methods specific to pet animals

# 'Dog' class inherits from 'Pets'     
class Dog(Pets):
    # Static method: can be called without creating an instance with parameters
    @staticmethod
    def bark():
        print("Bow Bow!!!!!")
 
 
# Create an object of the Dog class
d = Dog()

# Call the bark method using the object
d.bark()  # Output: Bow Bow!!!!!



"""
🔍 Key Concepts Explained:
class: Used to define a blueprint for objects (like Animals, Pets, Dog).
pass: Placeholder when you don't want to write any code yet.
@staticmethod: A method that doesn’t need access to the class or instance. You can call it directly from the class or an object.

=> Inheritance:
Pets inherits from Animals (meaning Pets is a kind of Animal).
Dog inherits from Pets (meaning Dog is a kind of Pet).
This is a basic example of multi-level inheritance.
"""