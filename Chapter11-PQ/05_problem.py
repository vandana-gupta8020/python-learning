# 5. Write a class vector representing a vector of n dimensions. Overload the '+' and '*' operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"Vetor({self.x}, {self.y}, {self.z})"

# test the implementation    
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)           # Same dimension vector
    
print("Addition of v1 & v2:", v1 + v2) 
print("Dot Product of v1 & v2:", v1 * v2)


print("Addition of v1 & v2:", v1 + v3) 
print("Dot Product of v1 & v2:", v1 * v3)

    
        



#---------------------------------------------------------------OR-----------------------------------------------------------------------------


class Vector:
    def __init__(self, data):
        self.data = data  # store the list of vector values

    def __add__(self, other):
        # '+' operator: Add corresponding values of two vectors
        result = [self.data[i] + other.data[i] for i in range(len(self.data))]
        return Vector(result)

    def __mul__(self, other):
        # '*' operator: Calculate dot product (multiply and sum)
        result = sum(self.data[i] * other.data[i] for i in range(len(self.data)))
        return result

    def __str__(self):
        return str(self.data)  # print vector nicely



v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("Addition:", v1 + v2)       # Output: [5, 7, 9]
print("Dot Product:", v1 * v2)    # Output: 32
