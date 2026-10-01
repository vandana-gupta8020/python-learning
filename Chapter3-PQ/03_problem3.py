# 3. Write a program to detect double space in a string.

a = "Python is compiler/interpreter programing language."
b = "Python is compiler/interpreter  programing language."

print(a.find("  "))     # output: -1 (If  got -1, which means double space doesn't exists)
print(b.find("  "))
print(a.find("compiler"))