''' Developers often have a need to interact with users, either to get data or to provide some sort
of result.  Most programs today use a dialog box as a way of asking the user to provide some type of
input.  While Python provides us with two inbuilt functions to read the input from the keyboard.

1. Raw Input raw_input ( ) : This function works in older version (like Python 2.x). This function
takes exactly what is typed from the keyboard,  convert it to string and then return it to the
variable in which we want to store.

2. Input


'''

# raw input g = raw_input("Enter your name: ") print g

# typecasting to integer
g = int(raw_input("Enter your age: "))

# typecasting to float
g = float(raw_input("Enter your marks in float : "))

# typecasting to string
g = str(raw_input("Enter your name : "))

''' Here, g is a variable which will get the string value,  typed by user during the execution of
program.  Typing of data for the raw_input() function is terminated by enter key.  We can use
raw_input() to enter numeric data also.  In that case we use typecasting. '''




# input 
''' input ( ) : This function first takes the input from the user and then evaluates the
expression,  which means Python automatically identifies whether user entered a string or a number
or list. 

If the input provided is not correct then either syntax error or exception is raised by python.

When input() function executes program flow will be stopped until the user has given an input. 

The text or message display on the output screen to ask a user to enter input value is optional 
i.e. the prompt, will be printed on the screen is optional. 

Whatever you enter as input, input function convert it into a string. if you enter an integer value
still input() function convert it into a string. You need to explicitly convert it into an integer
in your code using typecasting.

'''

num = input("Enter number : ")
print(num)

name1 = input("Enter number : ")
print(name1)

print("type of number", type(num))
print("type of name",type(name1))
