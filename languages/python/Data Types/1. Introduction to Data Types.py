# strings in python 

'''
A string is a sequence of characters. It can be declared in python by
using  double quotes. Strings are immutable, i.e., they cannot be
changed. 
''' 

# a simple string definition
a = "this is a string" 
print a


# Lists in Python

'''
Lists are one of the most powerful tools in python. They are just like
the arrays declared in other languages. But the most powerful thing is
that list need not be always homogenous. A single list can contain
strings, integers, as well as objects. Lists can also be used for
implementing stacks and queues. Lists are mutable, i.e., they can be
altered once declared.
'''

# declaring a simple list
L = [1, "a", "string", 1+3]

# adding one element to the list
L.append(6)

# removing one element from the list
L.pop()

# Tuples in python

'''
A tuple is a sequence of immutable Python objects. Tuples are just
like lists with the exception that tuples cannot be changed once
declared. Tuples are usually faster than lists.
'''
tup = (1, "a", "string", 1+3)
print tup
print tup[1]

# Iterations in Python
'''
Iterations or looping can be performed in python by ‘for’ and ‘while’
loops. Apart from iterating upon a particular condition, we can also
iterate on strings, lists, and tuples.
'''

# a simple while loop
i = 0
while i<10 :
	print(i)
	i = i+1

# looping on string
s = "hello world"
for i in s:
	print(i)

# looping on list
List = [1, 4, 5]
for i in List:
	print(i)

# using the range operator for looping on a list
for i in range(0,10):
	print(i)
