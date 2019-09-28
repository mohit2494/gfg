'''
In Python, Strings are arrays of bytes representing Unicode
characters. However, Python does not have a character data type, a
single character is simply a string with a length of 1. 

Square brackets can be used to access elements of the string.

Strings in Python can be created using single quotes or double quotes
or even triple quotes.

String in single quotes cannot hold any other single quoted character
in it otherwise an error arises because the compiler won’t recognize
where to start and end the string. To overcome this error, use of
double quotes is preferred, because it helps in creation of Strings
with single quotes in them. For strings which contain Double quoted
words in them, use of triple quotes is suggested. Along with this,
triple quotes also allow the creation of multiline string
'''
# Python Program for 
# Creation of String 
  
# Creating a String  
# with single Quotes 
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ") 
print(String1) 
  
# Creating a String 
# with double Quotes 
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ") 
print(String1) 
  
# Creating a String 
# with triple Quotes 
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ") 
print(String1) 
  
# Creating String with triple 
# Quotes allows multiple lines 
String1 = '''Geeks 
            For 
            Life'''
print("\nCreating a multiline String: ") 
print(String1)


# accessing strings in python

'''
In Python, individual characters of a String can be accessed by using
the method of Indexing, to access a range of characters in the String,
method of slicing is used. Slicing in a String is done by using a
Slicing operator (colon). Indexing allows negative address references
to access characters from the back of the String, e.g. -1 refers to
the last character, -2 refers to the second last character and so on.
While accessing an index out of the range will cause an IndexError.
Only Integers are allowed to be passed as an index, float or other
types will cause a TypeError.
'''

# Python Program to Access 
# characters of String 
  
String1 = "GeeksForGeeks"
print("Initial String: ") 
print(String1) 
  
# Printing First character 
print("\nFirst character of String is: ") 
print(String1[0]) 
  
# Printing Last character 
print("\nLast character of String is: ") 
print(String1[-1]) 
  
# Printing 3rd to 12th character 
print("\nSlicing characters from 3-12: ") 
print(String1[3:12]) 
  
# Printing characters between  
# 3rd and 2nd last character 
print("\nSlicing characters between " +
    "3rd and 2nd last character: ") 
print(String1[3:-2])


# deleting or updating strings in python
'''
In Python, Updation or deletion of characters from a String is not
allowed. This will cause an error because item assignment or item
deletion from a String is not supported. Although deletion of entire
String is possible with the use of a built-in del keyword. This is
because Strings are immutable, hence elements of a String cannot be
changed once it has been assigned. Only new strings can be reassigned
to the same name.
'''

# Python Program to Update 
# character of a String 

String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 

# Updating a character 
# of the String 
String1[2] = 'p'
print("\nUpdating character at 2nd Index: ") 
print(String1) 

# updating entire string

# python program to update entire string

String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 

# Updating a String 
String1 = "Welcome to the Geek World"
print("\nUpdated String: ") 
print(String1) 

# Deletion of a character
# Python Program to Delete 
# characters from a String 
  
String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 
  
# Deleting a character  
# of the String 
del String1[2]  
print("\nDeleting character at 2nd Index: ") 
print(String1) 


#Deleting Entire String:
'''
Deletion of entire string is possible with the use of del keyword.
Further, if we try to print the string, this will produce an error
because String is deleted and is unavailable to be printed
'''
# Python Program to Delete 
# entire String 

String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 

# Deleting a String 
# with the use of del 
del String1 
print("\nDeleting entire String: ") 
print(String1) 


# escape sequencing in python3
'''
While printing Strings with single and double quotes in it causes
SyntaxError because String already contains Single and Double Quotes
and hence cannot be printed with the use of either of these. Hence, to
print such a String either Triple Quotes are used or Escape sequences
are used to print such Strings. Escape sequences start with a
backslash and can be interpreted differently. If single quotes are
used to represent a string, then all the single quotes present in the
string must be escaped and same is done for Double Quotes. To ignore
the escape sequences in a String, r or R is used, this implies that
the string is a raw string and escape sequences inside it are to be
ignored.
'''
# Python Program for 
# Escape Sequencing  
# of String 
  
# Initial String 
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes: ") 
print(String1) 
  
# Escaping Single Quote  
String1 = 'I\'m a "Geek"'
print("\nEscaping Single Quote: ") 
print(String1) 
  
# Escaping Doule Quotes 
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ") 
print(String1) 
  
# Printing Paths with the  
# use of Escape Sequences 
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ") 
print(String1) 
  
# Printing Geeks in HEX 
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ") 
print(String1) 
  
# Using raw String to  
# ignore Escape Sequences 
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ") 
print(String1)



# string formatting - not that useful for competitive programming
# but can be useful in general

'''
Strings in Python can be formatted with the use of format() method which is
very versatile and powerful tool for formatting of Strings. Format method in
String contains curly braces {} as placeholders which can hold arguments
according to position or keyword to specify the order. A string can be
left(<), right(>) or center(^) justified with the use of format specifiers,
separated by colon(:). Integers such as Binary, hexadecimal, etc. and floats
can be rounded or displayed in the exponent form with the use of format
specifiers.
'''


# Python Program for 
# Formatting of Strings 

# Default order 
String1 = "{} {} {}".format('Geeks', 'For', 'Life') 
print("Print String in default order: ") 
print(String1) 

# Positional Formatting 
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life') 
print("\nPrint String in Positional order: ") 
print(String1) 

# Keyword Formatting 
String1 = "{l} {f} {g}".format(g = 'Geeks', f = 'For', l = 'Life') 
print("\nPrint String in order of Keywords: ") 
print(String1) 

# Formatting of Integers 
String1 = "{0:b}".format(16) 
print("\nBinary representation of 16 is ") 
print(String1) 

# Formatting of Floats 
String1 = "{0:e}".format(165.6458) 
print("\nExponent representation of 165.6458 is ") 
print(String1) 

# Rounding off Integers 
String1 = "{0:.2f}".format(1/6) 
print("\none-sixth is : ") 
print(String1) 

# String alignment 
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks','for','Geeks') 
print("\nLeft, center and right alignment with Formatting: ") 
print(String1) 

# There are numerous built-in functions in python for strings

# complete list : https://www.geeksforgeeks.org/python-strings/
