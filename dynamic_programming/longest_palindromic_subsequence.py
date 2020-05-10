"""
PROBLEM STATEMENT
-----------------
Given a String, find the longest palindromic subsequence

Input:
The first line of input contains an integer T, denoting no of test cases. The only line of each test case consists of a string S(only lowercase)

Output:
Print the Maximum length possible for palindromic subsequence.

Constraints:
1<=T<=100
1<=|Length of String|<=1000
 

Examples:
Input:
2
bbabcbcab
abbaab
Output:
7

LOGIC
-----
The naive solution for this problem is to generate all subsequences of given sequence and find the longest palindromic subsequence. But this solution is exponential in terms of time complexity.
    Recursive solution:
//Every single character is a palindrome of length 1
L(i,i) = 1 for all indexes i in given sequence

//If first and last characters are not same
If (C[i] != C[j]) L(i,j) = max(L(i+1,j),L(i,j-1))

//If there are only two characters and both are same
Else if(j == i+1) L(i,j) = 2

//If there are more tha two character and first and last characters are same
Else L(i, j) = L(i+1,j-1)+2

              L(0, 5)
             /        \ 
            /          \  
        L(1,5)          L(0,4)
       /    \            /    \
      /      \          /      \
  L(2,5)    L(1,4)  L(1,4)  L(0,3)

Since there are overlapping subproblems we can derive a dynamic problem solution to it.



SOURCE
------
geeksforgeeks

CODE
----
"""

def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0 for i in range(n)]for j in range(n)]
    
    for i in range(n):
        dp[i][i] = 1 #single character palindrome
        
    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            if s[i]==s[j] and l ==2:
                dp[i][j] = 2#subsequence of length 2 with same characters
                
            elif s[i]==s[j]:
                dp[i][j] = dp[i+1][j-1]+2
                
            else:
                dp[i][j] = max(dp[i][j-1],dp[i+1][j])
                
    return dp[0][n-1]

t = int(input())
for _ in range(t):
    s = input()
    print(longest_palindromic_subsequence(s))
