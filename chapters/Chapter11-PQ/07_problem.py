# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.


class Vector:
    def __init__(self, list):
        self.list = list
        
        
        
    def __len__(self):
        return len(self.list)
        

# test the implementation    
v1 = Vector([1, 2, 3])
print(len(v1))



#--------------------------------------------------------OR------------------------------------------------------------------------------------


class Vector:
    def __init__(self, data):
        self.data = data  # store list of vector values

    def __add__(self, other):
        # '+' operator: Add values element-wise
        result = [self.data[i] + other.data[i] for i in range(len(self.data))]
        return Vector(result)

    def __mul__(self, other):
        # '*' operator: Dot product (multiply and sum)
        result = sum(self.data[i] * other.data[i] for i in range(len(self.data)))
        return result

    def __len__(self):
        # Return dimension of vector
        return len(self.data)

    def __str__(self):
        return str(self.data)  # display vector nicely


# Example
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("Addition:", v1 + v2)       # Output: [5, 7, 9]
print("Dot Product:", v1 * v2)    # Output: 32
print("Dimension of v1:", len(v1))  # Output: 3
