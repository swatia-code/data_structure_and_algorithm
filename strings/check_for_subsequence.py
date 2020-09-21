'''
PROBLEM STATEMENT
-----------------
Given two strings A and B, find if A is a subsequence of B.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two space separated strings A and B.

Output:
For each test case, in a new line, print 1 if a is sub-sequences of b else print 0.

Constraints:
1 <= T <= 900
1<= |A|,|B| <=104

Example:
Input:
2
AXY YADXCP
gksrek geeksforgeeks

Output:
0
1

Explanation:
Testcase1:
Input: A = "axy", B = "yadxcp"
Output: 0 (A is not a subsequence of B)
Testcase2:
Input: A = "gksrek", B = "geeksforgeeks"
Output: 1 (str1 is a subsequence of str2)


LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
def is_subsequence(s1, s2):
    n = len(s1)
    m = len(s2)
    
    i = 0
    j = 0
    
    while(i < n and j < m):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            j += 1
            
    if i == n:
        return True
    else:
        return False
        
    
t = int(input())
for _ in range(t):
    s1, s2 = list(map(str, input().split()))
    res = 1 if is_subsequence(s1, s2) else 0
    print(res)
