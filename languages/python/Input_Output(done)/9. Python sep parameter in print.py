''' The separator between the arguments to print() function in Python is space by default (softspace
feature) , which can be modified and can be made to any character, integer or string as per our
choice. The ‘sep’ parameter is used to achieve the same, it is found only in python 3.x or later. It
is also used for formatting the output strings. '''

# code for disabling softspace feature
print('G', 'F', 'G', sep = '')

# for formatting a date
print('12','Dec','1994', sep = '-')

# another example
print('mohit','geeksforgeeks', sep='@')
#mohit@geeksforgeeks