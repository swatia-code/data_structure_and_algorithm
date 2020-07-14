'''
PROBLEM STATEMENT
-----------------
Given a string S. The task is to print all permutations of a given string.

Input:
The first line of input contains an integer T, denoting the number of test cases. Each test case contains a single string S in capital letter.

Output:
For each test case, print all permutations of a given string S with single space and all permutations should be in lexicographically increasing order.

Constraints:
1 ≤ T ≤ 10
1 ≤ size of string ≤ 5

Example:
Input:
2
ABC
ABSG

Output:
ABC ACB BAC BCA CAB CBA 
ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA

Explanation:
Testcase 1: Given string ABC has permutations in 6 forms as ABC, ACB, BAC, BCA, CAB and CBA .

LOGIC
-----
backtracking

SOURCE
------
geeksforgeeks

CODE
----
'''
def permute(a, l, r, lis): 
    if l==r: 
        lis.append(a) 
    else: 
        for i in range(l,r+1): 
            a = list(a)
            a[i], a[l] = a[l], a[i]
            a = "".join(a)
            permute(a, l+1, r, lis) 
            a = list(a)
            a[i], a[l] = a[l], a[i]
            a = "".join(a)
			
        
t = int(input())
for _ in range(t):
    s = input()
    lis = list()
    permute(s, 0, len(s) - 1, lis)
    for ele in sorted(lis):
        print(ele, end = " ")
    print()
