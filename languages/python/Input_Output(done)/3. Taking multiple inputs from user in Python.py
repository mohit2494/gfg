''' 

Developer often wants a user to enter multiple values or inputs in one line.
In C++/C user can take multiple inputs in one line using scanf but in Python
user can take multiple values or inputs in one line by two methods.

- using the split() method 
- using List Comprehension

'''


# using split method  

''' 
This function helps in getting a multiple inputs from
user . It breaks the given input by the specified separator. 
If separator is not provided then any white space is a separator.
Generally, user use a split() method to split a Python string but 
one can used it in taking multiple input.

'''
# syntax : 
input().split(seperator, maxsplit)

# python program showing how to 
# multiple input using  split

# taking two inputs at a time
x, y = input("Enter 2 values").split()

# taking three inputs at a time
x, y, z = input("Enter 3 values").split()

# how to print the input value using 
'''
str.format()  is an improvement on %-formatting. It uses normal 
function call syntax and is extensible through the __format__() 
method on the object being converted to a string.
'''

# taking two inputs at a time and printing them
a, b = input('Enter 2 values : ').split()
print("First number is {} and second number is {}".format(a,b))

# taking multiple inputs at a time
# and typecasting using list function

# we are converting the input to string
# to help us manage input effectively
x = list(map(int,input('Enter multiple values : ').split()))
print('List of values',x)


# second way is using list comprehensions

# taking two inputs at a time
x,y = [int(x) for x in input('Enter your values').split()]

# similarly taking 3 inputs at a time
x, y, z = [int(x) for x in input('Enter your values').split()]

# taking multiple values at a time
x = [int(x) for x in input('Enter multiple values').split()]
print('values in list are :',x)
