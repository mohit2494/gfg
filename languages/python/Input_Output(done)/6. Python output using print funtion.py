''' 
The simplest way to produce output is using the print() function where you can pass zero or more expressions separated by commas. This function converts the expressions you pass into a string before writing to the screen. 

'''

# syntax
print(values, sep = '', end = '\n', flush = flush)

'''

- values - any value and as many values as you like.
All values will be converted to string before getting
printed.

- sep - optional - how to seperate more than one values. Default : ''

- end - optional - specifies what to print in the end. Default : '\n'

- file - optional - an object with a write method. Default : sys.stdout

- flush - optional - A boolean specifying if the output is flushed (True) or buffered
(False). Default : False


The print() function returns the output to the screen
'''

# Python 3.x program showing
# how to print data on a screen

# one object is passed
print('mohit kalra')
# mohit kalra

x = 5
print('x = ',x)
# x = 5

print('Mohit','Kalra',sep=' ')
# Mohit Kalra

print('Mohit',end='@')
# Mohit@
