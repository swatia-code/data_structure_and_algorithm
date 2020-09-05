'''
PROBLEM STATEMENT
-----------------
Given a string, a partitioning of the string is a palindrome partitioning if every sub-string of the partition is a palindrome. For example, “aba|b|bbabb|a|b|aba” is a palindrome partitioning of “ababbbabbababa”. Determine the fewest cuts needed for palindrome partitioning of a given string. For example, minimum 3 cuts are needed for “ababbbabbababa”. The three cuts are “a|babbbab|b|ababa”.

Input:
The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. The first line of every Test Case consists of S, denoting a String.

Output:
For each test case in a new line print an integer, denoting the number cuts in the String to make it palindromic.

Constraints:
1<=T<=100
1<=|Length of String|<=1000

Example:
Input:
2
ababbbabbababa
aaabba

Output:
3
1

LOGIC
-----
Recursion behind the solution is:
-> when the string is palindrome(1. single character 2. complete string is palindrome) return 0
-> Else make cuts at all possible places and recursively calculate the cose for each cut and return the minimum cost

#Base case
min_pal_pat(s, i, j) = 0 when i == j or s[i...j] is a palindrome

#Recursive step
min_pal_pat(s, i, j) = min(min_pal_pat(s, i, k) + 1 + min_pal_pat(s, k + 1, j))
where k is from i to j - 1

Since we encounter overlapping subproblems we can use dynamic programming to calculate the minimum cost


SOURCE
------
geeksforgeeks

CODE
----
'''
def min_pal_part(s):
    n = len(s)
    
    pal = [[False for j in range(n)] for i in range(n)]
    count = [[0 for j in range(n)] for i in range(n)]
    
    ans = 0
    
    for i in range(n):
        pal[i][i] = True
        count[i][i] = 0
        
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            
            if L == 2:
                pal[i][j] = (s[i] == s[j])
            else:
                pal[i][j] = ((s[i] == s[j]) and P[i + 1][j - 1])
                
            if pal[i][j]:
                count[i][j] = 0
            else:
                count[i][j] = float('inf')
                for k in range(i, j):
                    count[i][j] = min(count[i][j], count[i][k] + count[k + 1][j] + 1)
                    
    return count[0][n - 1]

t = int(input())
for _ in range(t):
    s = input()
    print(min_pal_part(s))

#other solution
def isPali(s, l, r):
    while l < r:
        if(s[l] != s[r]): return False
        l += 1
        r -= 1
    return True
for _ in range(int(input().strip())):
    s = input().strip()
    n = len(s)
    pali = [[False]*n for i in range(n)]
    for i in range(n):
        for j in range(i+1):
            pali[i][j] = pali[j][i] = isPali(s, j, i)
    dp = [float('inf')]*(n+1)
    dp[0] = 0
    for i in range(n):
        for j in range(i+1):
            if(pali[i][j]): dp[i+1] = min(dp[i+1], dp[j]+1)
    print(dp[-1]-1)
            
    
