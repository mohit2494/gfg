'''
Given a string, count number of subsequences of the form 
a^ib^jc^k, i.e., it consists of i ’a’ characters, followed by 
j ’b’ characters, followed by k ’c’ characters where i >= 1, j >=1 and k >= 1.

Note: Two subsequences are considered different if the set of array indexes 
picked for the 2 subsequences are different.

Expected Time Complexity : O(n)

Input  : abbc
Output : 3
Subsequences are abc, abc and abbc

Input  : abcabc
Output : 7
Subsequences are abc, abc, abbc, aabc,abcc, abc and abc

Going from left to right, keep track of the number of sequences until the current position, 
which are of these three forms:
a^i
a^i b^j
a^i b^j c^k 
Suppose that these are stored in three variables a,b,c respectively. Whenever you see the character ‘a’, 
it can extend the strings of type 1, and also, be the starting position for a string of type 1, 
so a+=(a+1), whenever you see a ‘b’, it can extend previous strings of type 1 and 2, so b+=(a+b), 
for ‘c’, it will extend all strings of type 2 and 3, so c+=(b+c).

'''
def all_subs(s):
    a, b , c = 0, 0, 0
    size = len(s)
    for i in range(size):
        if s[i] == 'a':
            a += a+1
        elif s[i] == 'b':
            b += (a+b)
        else:
            c += (b+c)
    return c
'''------------------------------------'''
s = "abcabc"
print(all_subs(s))

'''
solution : https://discuss.codechef.com/t/help-needed-for-solving-string-and-sub-sequences-problem/14057
'''