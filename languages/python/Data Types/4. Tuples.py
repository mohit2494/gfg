'''
Tuple is a collection of Python objects much like a list. The sequence of
values stored in a tuple can be of any type, and they are indexed by integers.

The important difference between a list and a tuple is that tuples are
immutable. 

--Also, Tuples are hashable whereas lists are not.--

Values of a tuple are syntactically separated by ‘commas’. Although it is not
necessary, it is more common to define a tuple by closing the sequence of
values in parentheses. This helps in understanding the Python tuples more
easily.

Tuples are immutable, and usually, they contain a sequence of heterogeneous
elements that are accessed via unpacking or indexing (or even by attribute in
the case of named tuples). Lists are mutable, and their elements are usually
homogeneous and are accessed by iterating over the list.
'''


# creating a tuple in python
# --------------------------

'''
In Python, tuples are created by placing sequence of values separated by
‘comma’ with or without the use of parentheses for grouping of data sequence.
Tuples can contain any number of elements and of any datatype (like strings,
integers, list, etc.). Tuples can also be created with a single element, but
it is a bit tricky. Having one element in the parentheses is not sufficient,
there must be a trailing ‘comma’ to make it a tuple.
'''

# Creating a Tuple in Python
# --------------------------
# Python program to demonstrate 
# Addition of elements in a Set 

# Creating an empty tuple 
Tuple1 = () 
print("Initial empty Tuple: ") 
print (Tuple1) 

# Creating a Tuple with 
# the use of Strings 
Tuple1 = ('Geeks', 'For') 
print("\nTuple with the use of String: ") 
print(Tuple1) 


# Creating a Tuple with 
# the use of list 
list1 = [1, 2, 4, 5, 6] 
print("\nTuple using List: ") 
print(tuple(list1)) 

# Creating a Tuple 
# with the use of loop 
Tuple1 = ('Geeks') 
n = 5
print("\nTuple with a loop") 
for i in range(int(n)): 
	Tuple1 = (Tuple1,) 
	print(Tuple1) 

# Creating a Tuple with the 
# use of built-in function 
Tuple1 = tuple('Geeks') 
print("\nTuple with the use of function: ") 
print(Tuple1) 

# Creating a Tuple with 
# Mixed Datatypes 
Tuple1 = (5, 'Welcome', 7, 'Geeks') 
print("\nTuple with Mixed Datatypes: ") 
print(Tuple1) 

# Creating a Tuple 
# with nested tuples 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('python', 'geek') 
Tuple3 = (Tuple1, Tuple2) 
print("\nTuple with nested tuples: ") 
print(Tuple3) 

# Creating a Tuple 
# with repetition 
Tuple1 = ('Geeks',) * 3
print("\nTuple with repetition: ") 
print(Tuple1) 


for i in range(1,int(raw_input())+1):
    print  reduce(lambda x, y: x + (10 ** (y - 1)), range(1, i + 1))**2


from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))


