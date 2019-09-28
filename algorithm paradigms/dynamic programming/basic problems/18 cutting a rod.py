# cutting rod problem - dynamic programming
'''
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if length of the rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)
'''


'''
1) Optimal Substructure: 
We can get the best price by making a cut at different positions and comparing the values obtained after a cut. We can recursively call the same function for a piece obtained after a cut.

Let cutRod(n) be the required (best possible price) value for a rod of length n. cutRod(n) can be written as following.

cutRod(n) = max(price[i] + cutRod(n-i-1)) for all i in {0, 1 .. n-1}

2) Overlapping Subproblems
Following is simple recursive implementation of the Rod Cutting problem. The implementation simply follows the recursive structure mentioned above.
'''

# basic recursion
import sys

def max(a,b):
	return a if (a>b) else b

def cut_rod(price, n):
	if n <= 0:
		return 0
	max_val = -sys.maxsize - 1
	for i in range(0,n):
		max_val = max(max_val,price[i]+cut_rod(price,n-i-1))
	return max_val

'''
cR() ---> cutRod() 

                             cR(4)
                  /        /           
                 /        /              
             cR(3)       cR(2)     cR(1)   cR(0)
            /  |         /         |
           /   |        /          |  
      cR(2) cR(1) cR(0) cR(1) cR(0) cR(0)
     /        |          |
    /         |          |   
  cR(1) cR(0) cR(0)      cR(0)
   /
 /
CR(0)

we are saving the same sub-problem multiple times
we shall now memoize a table bottom up
'''

# dynamic programming
def cut_rod_dp(price, n):
	val = [0 for x in range(n+1)]
	val[0] = 0
	for i in range(1,n+1):
		max_val = -sys.maxsize - 1
		for j in range(i):
			max_val = max(max_val, price[j] + val[i-j-1])
		val[i] = max_val
	return val[n]

arr = [1,5,8,9,10,17,17,20]
size = len(arr)
print(cut_rod_dp(arr, size))



	