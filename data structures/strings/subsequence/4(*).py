'''
Given a string consisting of digits 0-9, count the number of subsequences in it divisible 
by m.

Examples:

Input  : str = "1234", n = 4
Output : 4
The subsequences 4, 12, 24 and 124 are 
divisible by 4.
 
Input  : str = "330", n = 6
Output : 4
The subsequences 30, 30, 330 and 0 are 
divisible by n.

Input  : str = "676", n = 6
Output : 3
The subsequences 6, 6 and 66
'''

'''
Brute force is all about generating all possible subsequences
and then checking whether the subsequence is divisible by n.

This problem can be recursively defined. Let remainder of a string with value x be ‘r’ 
when divided with n. Adding one more character to this string changes its remainder to 
(r*10 + newdigit) % n. For every new character, we have two choices, either add it in 
all current subsequences or ignore it. Thus, we have an optimal substructure. Following 
shows the brute force version of this:
'''

'''recursive solution'''
def num_subs_recursive(s, r, i, l, div,string=""):
    if i == l:
        #print("String",string,end="\n")
        #print("Remainder",r)
        return 1 if r is 0 else 0
    ans = 0
    if i is not l-1 or r!=0:
        ans += num_subs_recursive(s, r, i+1, l, div,string)
    ans += num_subs_recursive(s, (r*10+int(s[i]))%div, i+1, l, div,string+s[i])
    return ans

'''
          input string = "330"

             (0,0) ===> at 0th index with 0 remainder
(exclude 0th /      (include 0th character)
 character) /      
       (1,0)      (1,3) ======> at index 1 with 3 as 
      (E)/  (I)     /(E)       the current remainder
     (2,0)  (2,3)   (2,3)
             |-------|
     These two subproblems overlap  
'''


''' dynamic programming top-down memoization'''
def nums_subs_dp(str, n):
    l = len(str)






''' dynamic programming bottom up table building'''
def nums_subs_dp_bu(str, n):
    l = len(str)

    '''making a table of index * remainders'''
    dp = [[0 for x in range(n)]
             for y in range(l)]

    dp[0][int(str[0])%n] += 1

    for i in range(1,l):
        
        '''for cases where subsequence starts with i'''
        dp[i][int(str[i])%n] += 1
        
        for j in range(n):
            print(dp)
            '''If I ignore the current subsequence'''
            dp[i][j] += dp[i-1][j]
            
            '''If I consider the current subsequence'''
            dp[i][(j*10+int(str[i]))%n] += dp[i-1][j]
    return dp[l-1][0]
'''-----------------------------------------------------'''
str1 = "330"
n = 6
print(num_subs_recursive(str1, 0, 0, len(str1), n))
print(nums_subs_dp_bu(str1, n))