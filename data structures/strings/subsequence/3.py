'''
Given a string, count number of subsequences of the form 
aibjck, i.e., it consists of i ’a’ characters, followed by 
j ’b’ characters, followed by k ’c’ characters where i >= 1, j >=1 and k >= 1.

Note: Two subsequences are considered different if the set of array indexes 
picked for the 2 subsequences are different.

Expected Time Complexity : O(n)

Input  : abbc
Output : 3
Subsequences are abc, abc and abbc

Input  : abcabc
Output : 7
Subsequences are abc, abc, abbc, aabc
abcc, abc and abc
'''