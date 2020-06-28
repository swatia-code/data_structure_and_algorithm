'''
PROBLEM STATEMENT
-----------------
Given two unsorted arrays A of size N and B of size M of distinct elements, the task is to find all pairs from both arrays whose sum is equal to X.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains 3 lines . The first line contains 3 space separated integers N, M, X. Then in the next two lines are space separated values of the array A and B respectively.

Output:
For each test case in a new line print the sorted space separated values of all the pairs u,v where u belongs to array A and v belongs to array B, such that each pair is separated from the other by a ',' without quotes also add a space after the ',' . If no such pair exist print -1.

Constraints:
1 <= T <= 100
1 <= N, M, X <= 106
-106 <= A, B <= 106

Example:
Input:
2
5 5 9
1 2 4 5 7
5 6 3 4 8
2 2 3
0 2
1 3
Output:
1 8, 4 5, 5 4
0 3, 2 1

Explanation:
Testcase 1: (1, 8), (4, 5), (5, 4) are the pairs which sum to 9.

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''

def find_pair(l1, l2, sum):
    freq_1 = dict()
    freq_2 = dict()
    
    l1.sort()
    for ele in l1:
        if ele not in freq_1:
            freq_1[ele] = 1
            
    for ele in l2:
        if ele not in freq_2:
            freq_2[ele] = 1
            
    res = ''
            
    for ele in l1:
        if sum-ele in freq_2:
            res = res+str(ele)+' '+str(sum-ele)+', '
            
    return res

t = int(input())
for _ in range(t):
    l = [int(x) for x in input().split()]
    sum = l[-1]
    l1 = [int(x) for x in input().split()]
    l2 = [int(x) for x in input().split()]
    res = find_pair(l1, l2, sum)
    if len(res) == 0:
        print("-1")
    else:
        print(res[:-2])
