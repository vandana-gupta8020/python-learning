# 4. Write a class 'Complex' to represent complex numbers, along with overloaded operators *+* and '*' which adds and multiplies them.


# Define a class named 'Complex' to represent complex numbers
class Complex:
    
    # Constructor: this method runs when an object is created
    # r = real part, i = imaginary part
    def __init__(self, r, i):
        self.r = r          # Assign real part
        self.i = i          # Assign imaginary part
        
        
    # Overload the '+' operator so we can add two complex numbers using c1 + c2
    def __add__(self, c2):
        # Add real parts and imaginary parts separately
        return Complex(self.r + c2.r, self.i + c2.i)
    
    
    # Overload the '*' operator to multiply two complex numbers using c1 * c2 
    def __mul__(self, c2):
        
        # Formula for multiplication:
        # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        real = self.r * c2.r - self.i * c2.i      # Real part: ac - bd
        imag = self.r * c2.i - self.i * c2.r      # Imaginary part: ad + bc
        return Complex(real, imag)                # Return result as a new Complex object
    
    # Customize how object is printed using print()
    def __str__(self):
        # Display complex number in form: a + bi
        return f"{self.r} + {self.i}i"
    
    
c1 = Complex(1, 3)       # Create first complex number: 1 + 3i
c2 = Complex(2, 5)       # Create second complex number: 2 + 5i 

# Use overloaded + operator to add c1 and c2
print("Addition:", c1 + c2)  # Output: 3 + 8i

# Use overloaded '*' operator to multiply c1 and c2
print("Multiplication:", c1 * c2)    # Output: -13 + 11i

