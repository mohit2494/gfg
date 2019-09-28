
'''

Lists in Python
---------------

Lists in Python can be created by just placing the sequence inside the
square brackets[]. Unlike Sets, list doesn’t need a built-in function
for creation of list. A list may contain duplicate values with their
distinct positions and hence, multiple distinct or duplicate values
can be passed as a sequence at the time of list creation.

Adding elements to a List
--------------------------

Elements can be added to the List by using built-in append() function. Only
one element at a time can be added to the list by using append() method, for
addition of multiple elements with the append() method, loops are used. Tuples
can also be added to the List with the use of append method because tuples are
immutable. Unlike Sets, Lists can also be added to the existing list with the
use of append() method.

append() method only works for addition of elements at the end of the List,
for addition of element at the desired position, insert() method is used.
Unlike append() which takes only one argument, insert() method requires two
arguments(position, value). Other than append() and insert() methods, there’s
one more method for Addition of elements, extend(), this method is used to add
multiple elements at the same time at the end of the list.

Note – append() and extend() methods can only add elements at the end.

Accessing elements from the List
--------------------------------
In order to access the list items refer to the index number.Use the index
operator [ ] to access an item in a list.The index must be an integer.Nested
list are accessed using nested indexing.

Removing elements from the List
-------------------------------
Elements can be removed from the List by using built-in remove() function but
an Error arises if element doesn’t exist in the set. Remove() method only
removes one element at a time, to remove range of elements, iterator is used.
Pop() function can also be used to remove and return an element from the set,
but by default it removes only the last element of the set, to remove element
from a specific position of the List, index of the element is passed as an
argument to the pop() method.

Note – Remove method in List will only remove the first occurrence of the
searched element.


Slicing of a List
-----------------
In Python List, there are multiple ways to print the whole List with all the
elements, but to print a specific range of elements from the list, we use
Slice operation. Slice operation is performed on Lists with the use of
colon(:). To print elements from beginning to a range use [:Index], to print
elements from end use [:-Index], to print elements from specific Index till
the end use [Index:], to print elements within a range, use [Start Index:End
Index] and to print whole List with the use of slicing operation, use [:].
Further, to print whole List in reverse order, use [::-1].

Note – To print elements of List from rear end, use Negative Indexes.
----

				List Methods
				------------


FUNCTION	DESCRIPTION
--------	-----------

Append()	Add an element to the end of the list
Extend()	Add all elements of a list to the another list
Insert()	Insert an item at the defined index
Remove()	Removes an item from the list
Pop()		Removes and returns an element at the given index
Clear()		Removes all items from the list
Index()		Returns the index of the first matched item
Count()		Returns the count of number of items passed as an argument
Sort()		Sort items in a list in ascending order
Reverse()	Reverse the order of items in the list
copy()		Returns a copy of the list

			Built-in functions with List
			----------------------------

FUNCTION	DESCRIPTION
--------	-----------
round()		Rounds off to the given number of digits and returns the floating
			point number

reduce()	apply a particular function passed in its argument to all of the list
			elements stores the intermediate result and only returns the final summation 
			value

sum()		Sums up the numbers in the list

ord()		Returns an integer representing the Unicode code point of the given
			Unicode character

cmp()		This function returns 1, if first list is “greater” than second list

max()		return maximum element of given list
min()		return minimum element of given list

all()		Returns true if all element are true or if list is empty

any()		Return true if any element of the list is true. if list is empty,
			return false

len()		Returns length of the list or size of the list

enumerate()	Returns enumerate object of list

accumulate()	apply a particular function passed in its argument to all of the
				list elements returns a list containing the intermediate results

filter()		tests if each element of a list true or not

map()			returns a list of the results after applying the given function to
				each item of a given iterable

lambda()		This function can have any number of arguments but only one
				expression, which is evaluated and returned.
'''


# adding elements to a list
# Python program to demonstrate 
# Addition of elements in a List 

# Creating a List 
# ===============
List = [] 
print("Intial blank List: ") 
print(List) 

# Addition of Elements 
# in the List 
List.append(1) 
List.append(2) 
List.append(4) 
print("\nList after Addition of Three elements: ") 
print(List) 

# Adding elements to the List 
# using Iterator 
for i in range(1, 4): 
	List.append(i) 
print("\nList after Addition of elements from 1-3: ") 
print(List) 

# Adding Tuples to the List 
List.append((5, 6)) 
print("\nList after Addition of a Tuple: ") 
print(List) 

# Addition of List to a List 
List2 = ['For', 'Geeks'] 
List.append(List2) 
print("\nList after Addition of a List: ") 
print(List) 

# Addition of Element at 
# specific Position 
# (using Insert Method) 
List.insert(3, 12) 
List2.insert(0, 'Geeks') 
print("\nList after performing Insert Operation: ") 
print(List) 

# Addition of multiple elements 
# to the List at the end 
# (using Extend Method) 
List.extend([8, 'Geeks', 'Always']) 
print("\nList after performing Extend Operation: ") 
print(List) 


# accessing elements from the List
# ================================
# Python program to demonstrate 
# accessing of element from list 

# Creating a List with 
# the use of multiple values 
List = ["Geeks", "For", "Geeks"] 

# accessing a element from the 
# list using index number 
print("Accessing a element from the list") 
print(List[0]) 
print(List[2]) 

# Creating a Multi-Dimensional List 
# (By Nesting a list inside a List) 
List = [['Geeks', 'For'] , ['Geeks']] 

# accessing a element from the 
# Multi-Dimensional List using 
# index number 
print("Acessing a element from a Multi-Dimensional list") 
print(List[0][1]) 
print(List[1][0]) 


List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks'] 

# accessing a element using 
# negative indexing 
print("Acessing element using negative indexing") 

# print the last element of list 
print(List[-1]) 

# print the third last element of list 
print(List[-3]) 


# Removing elements from a list
# =============================

# Python program to demonstrate 
# Removal of elements in a List 

# Creating a List 
List = [1, 2, 3, 4, 5, 6, 
		7, 8, 9, 10, 11, 12] 
print("Intial List: ") 
print(List) 

# Removing elements from List 
# using Remove() method 
List.remove(5) 
List.remove(6) 
print("\nList after Removal of two elements: ") 
print(List) 

# Removing elements from List 
# using iterator method 
for i in range(1, 5): 
	List.remove(i) 
print("\nList after Removing a range of elements: ") 
print(List) 

# Removing element from the 
# Set using the pop() method 
List.pop() 
print("\nList after popping an element: ") 
print(List) 

# Removing element at a 
# specific location from the 
# Set using the pop() method 
List.pop(2) 
print("\nList after popping a specific element: ") 
print(List) 




# Slicing Python Lists
# --------------------
# Python program to demonstrate 
# slicing of elements in a List 

# Creating a List 
List = ['G','E','E','K','S','F', 
		'O','R','G','E','E','K','S'] 
print("Intial List: ") 
print(List) 

# Print elements of a range 
# using Slice operation 
Sliced_List = List[3:8] 
print("\nSlicing elements in a range 3-8: ") 
print(Sliced_List) 

# Print elements from beginning 
# to a pre-defined point using Slice 
Sliced_List = List[:-6] 
print("\nElements sliced till 6th element from last: ") 
print(Sliced_List) 

# Print elements from a 
# pre-defined point to end 
Sliced_List = List[5:] 
print("\nElements sliced from 5th "
	"element till the end: ") 
print(Sliced_List) 

# Printing elements from 
# beginning till end 
Sliced_List = List[:] 
print("\nPrinting all elements using slice operation: ") 
print(Sliced_List) 

# Printing elements in reverse 
# using Slice operation 
Sliced_List = List[::-1] 
print("\nPrinting List in reverse: ") 
print(Sliced_List) 


# There is a range of list programs in python
# access it here : https://www.geeksforgeeks.org/python-list/