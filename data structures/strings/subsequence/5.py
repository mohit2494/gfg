'''
Find number of times a string occurs as a subsequence in given string
Given two strings, find the number of times the second string occurs 
in the first string, whether continuous or discontinuous.

Examples:

Input:  
string a = "GeeksforGeeks"
string b = "Gks"

Output: 4

Explanation:  
The four strings are - (Check characters marked in bold)
GeeksforGeeks
GeeksforGeeks
GeeksforGeeks
GeeksforGeeks
'''

'''
this problem can be solved in similarity with the longest common subsequence
m: Length of str1 (first string)
n: Length of str2 (second string)

If last characters of two strings are same, 
   1. We consider last characters and get count for remaining 
      strings. So we recur for lengths m-1 and n-1. 
   2. We can ignore last character of first string and 
      recurse for lengths m-1 and n.
else 
If last characters are not same, 
   We ignore last character of first string and 
   recurse for lengths m-1 and n.
'''

def count(a, b, m, n):
    if (m == 0 and n == 0) or n == 0:
        return 1
    if m == 0:
        return 0
    if a[m-1] == b[n-1]:
        return count(a,b,m-1,n-1) + count(a,b,m-1,n)
    else:
        '''keep searching'''
        return count(a,b,m-1,n)

'''
the time complexity of above solution is exponential. I drew the recursion
tree and saw that the problems were overlapping. following is a dynamic
programming implementation of the above recursion.
'''
def count_dp(a, b, m, n):
    '''lookup table'''
    lookup = [[0]*(n+1) for i in range(m+1)]

    '''if first string in empty'''
    for i in range(n+1):
        lookup[0][i] = 0

    '''if second string is empty'''
    for i in range(m+1):
        lookup[i][0] = 1
    
    ''' for all rows'''
    for i in range(1,m+1):
        '''for all columns'''
        for j in range(1,n+1):
            if a[i-1] == b[j-1]:
                # print(lookup)
                lookup[i][j] = lookup[i-1][j-1] + lookup[i-1][j]
            else:
                lookup[i][j] = lookup[i-1][j]
    return lookup[m][n]
'''---------------------------------------'''
a = "GeeksforGeeks"
b = "Gks"
print(count_dp(a, b, len(a), len(b)))

