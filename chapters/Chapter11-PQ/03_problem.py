# Ques. 3
"""
Create a class 'Employee' and add salary and increment properties to it.

Write a method 'salaryAfterIncrement' method with a @property decorator with a setter which changes the value of increment based on the salary."""


# Create a class named 'Employee'
class Employee:
    salary = 120000        # Base salary
    increment = 20         # Initial increment percentage
    
    
    # This method calculates salary after applying the increment
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    
    # This setter updates the increment value when new salary is given
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        # Formula to find new increment based on given salary
        self.increment = ((salary/self.salary) - 1)*100              #  Formula: new salary = old salary (1 + increment/100)

            

# Create an object of Employee class
e = Employee()

# print(e.salaryAfterIncrement)


# Set a new salary — this will update the increment percentage
e.salaryAfterIncrement = 144000.0

# Print the new increment percentage
print(e.increment)  # Output will be around 20%               # output = 19.999999999999996







