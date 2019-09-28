''' By default python’s print() function ends with a newline. A programmer with C/C++ background may
wonder how to print without newline.

Python’s print() function comes with a parameter called ‘end’. By default, the value of this
parameter is ‘\n’, i.e. the new line character. You can end a print statement with any
character/string using this parameter. '''


print("Python", end = '@')
print("geeksforgeeks")

# Python@geeksforgeeks
