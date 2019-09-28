'''
Given two strings str1 and str2, find if str1 is a subsequence 
of str2. A subsequence is a sequence that can be derived from 
another sequence by deleting some elements without changing 
the order of the remaining elements (source: wiki). Expected 
time complexity is linear.

Input: str1 = "AXY", str2 = "ADXCPY"
Output: True (str1 is a subsequence of str2)

Input: str1 = "AXY", str2 = "YADXCP"
Output: False (str1 is not a subsequence of str2)

Input: str1 = "gksrek", str2 = "geeksforgeeks"
Output: True (str1 is a subsequence of str2)
'''

# iterative
def is_subsequence(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    if len1 == 0:
        return True
    if len2 == 0:
        return False

    i, j = 0, 0
    ans = False
    while i < len1 and j < len2:
            if str1[i] == str2[j]:
                i += 1
            j += 1
    
    if i == len1:
        print("True")
    else:
        print("False")


# str1 = "AXY"
# str2 = "ADXCPY"
# is_subsequence(str1, str2)

str1 = "AXY"
str2 = "YADXCP"
is_subsequence(str1, str2)