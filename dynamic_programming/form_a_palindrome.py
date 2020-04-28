"""
PROBLEM
-------
Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd
Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is S.
Output:
Print the minimum number of characters.
Constraints:
1 ≤ T ≤ 50
1 ≤ S ≤ 40
Example:
Input:
3
abcd
aba
geeks
Output:
3
0
3

LOGIC
-----
In https://github.com/swatia-code/data_structure_and_algorithm/blob/master/recursion/form_a_palindrome_recursive.py if we observe this approach carefully, we can find that it exhibits overlapping subproblems. Memoization technique is used to avaoid similar subproblem recalls. We can create a table to store results of subprblems so that they can be used directly if same subproblem is encountered again.

CODE
----
"""
def form_palindrome(str):
    pal = [[0 for i in range(len(str))] for j in range(len(str))]
    
    for gap in range(1,len(str)):
        l = 0
        for h in range(gap,len(str)):
            if str[l] == str[h]:
                pal[l][h] = pal[l+1][h-1]
            else:
                pal[l][h] = min(pal[l][h-1],pal[l+1][h])+1
            l+=1
                
    return pal[0][len(str)-1]
        

t = int(input())

for _ in range(t):
    s = input()
    print(form_palindrome(s))


