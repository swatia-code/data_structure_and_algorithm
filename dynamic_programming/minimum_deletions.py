'''
PROBLEM STATEMENT
-----------------
Given a string of S as input. Your task is to write a program to remove or delete minimum number of characters from the string so that the resultant string is palindrome.

Note: The order of characters in the string should be maintained.

Input:
First line of input contains a single integer T which denotes the number of test cases. Then T test cases follows. First line of each test case contains a string S.

Output:
For each test case, print the deletions required to make the string palindrome.

Constraints:
1<=T<=100
1<=length(S)<=10000

Example:
Input:
2
aebcbda
geeksforgeeks
Output:
2
8

LOGIC
-----
-->str is the given string.
-->n length of str
-->len be the length of the longest 
   palindromic subsequence of str
-->// minimum number of deletions 
   min = n - len

SOURCE
------
geeksforgeeks

CODE
----
'''
def longest_palindromic_subsequence(s):
    
    n = len(s)
    
    dp = [[0 for i in range(n)]for j in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
        
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j] and l == 2:
                dp[i][j] == 2
                
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
                
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                
                
    return dp[0][n - 1]
            

def minimum_deletions(s):
    l = len(s)
    n = longest_palindromic_subsequence(s)
    
    return l - n

t = int(input())
for _ in range(t):
    s = input()
    print(minimum_deletions(s))
