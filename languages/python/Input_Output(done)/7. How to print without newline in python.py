''' 
Generally people switching from C/C++ to Python wonder how to print two or more variables or
statements without going into a new line in python. Since the python print() function by default
ends with newline. Python has a predefined format if you use print(a_variable) then it will go to
next line automatically.

'''

# Print without newline in Python 3.x

# The default end of the print() statement in python3
# is \n
print("geeks", end=" ")
print("geeksforgeeks")

# geeks geeksforgeeks

for i in range(4):
	print(i, end = ' ')
# 1 2 3 4