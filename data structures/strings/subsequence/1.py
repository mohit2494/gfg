'''
Given a string and a number k, find the longest subsequence of a string where every character appears at-least k times.
Input : str = "geeksforgeeks"
         k = 2
Output : geeksgeeks
Every character in the output
subsequence appears at-least 2
times.

Input : str = "aabbaabacabb"
          k = 5
Output : aabbaabaabb
'''
#--------------------------------------------------
max_chars = 26

def longestSubsequenceWithK(str, k):
    
    n = len(str)
    freq = [0]*max_chars
    
    for i in range(n):
        index = ord(str[i]) - ord('a')
        freq[index] +=1

    for i in range(n):
        index = ord(str[i]) - ord('a')
        if freq[index] >= k:
            print(str[i], end="")

    print("",end="\n")

#-------------------------------------------------
str = "geeksforgeeks"
k = 2
longestSubsequenceWithK(str, k)

str = "aabbaabacabb"
k = 5
longestSubsequenceWithK(str, k)