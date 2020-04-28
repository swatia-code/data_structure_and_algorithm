"""
PROBLEM STATEMENT
-----------------
Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.

Input:
First line of the input contains no of test cases  T,the T test cases follow.
Each test case consist of 2 space separated integers A and B denoting the size of string str1 and str2 respectively
The next two lines contains the 2 string str1 and str2 .

Output:
For each test case print the length of longest  common subsequence of the two strings .

Constraints:
1<=T<=200
1<=size(str1),size(str2)<=100

Example:
Input:
2
6 6
ABCDGH
AEDFHR
3 2
ABC
AC

Output:
3
2

Explanation
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.

LCS of "ABC" and "AC" is "AC" of length 2

LOGIC
-----
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
It is a classic computer science problem, the basis of diff (a file comparison program that outputs the difference between two files) and has applications in bioinformatics.

The naive solution for this problem is to generate all subsequences of both given subsequences and then find the longest matching subsequence. This solution is exponential in term of time complexity.


SOURCE
------
geeksforgeeks

CODE
----
"""

#code
def longest_common_subsequence(s1,s2):
    n = len(s1)
    m = len(s2)
    
    lcs = [[0 for i in range(n+1)] for j in range(m+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s2[i-1] == s1[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
                    
    return lcs[m][n]

t = int(input())
for _ in range(t):
    num = input()
    s1 = input()
    s2 = input()
    print(longest_common_subsequence(s1,s2))

