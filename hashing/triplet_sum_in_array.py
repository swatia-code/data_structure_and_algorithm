'''
PROBLEM STATEMENT
-----------------
Given an array A[] of N numbers and another number x, determine whether or not there exist three elements in A[] whose sum is exactly x.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains n and x. Next line contains array elements.

Output:
Print 1 if there exist three elements in A whose sum is exactly x, else 0.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 103
1 ≤ A[i] ≤ 105

Example:
Input:
2
6 13
1 4 45 6 10 8
5 10
1 2 4 3 6

Output:
1
1

Explanation:
Testcase 1: There is one triplet with sum 13 in the array. Triplet elements are 1, 4, 8, whose sum is 13.

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
def triplet(l, s):
    freq = dict()
    for ele in l:
        if ele not in freq:
            freq[ele] = 1
        else:
            freq[ele] += 1
            
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            val = s - l[i] - l[j]
            if val in freq:
                if val == l[i]:
                    if freq[l[i]] == 1:
                        continue
                if val == l[j]:
                    if freq[l[j]] == 1:
                        continue
                return True
                
    return False

t = int(input())
for _ in range(t):
    l = [int(x) for x in input().split()]
    n = l[0]
    s = l[1]
    l1 = [int(x) for x in input().split()]
    if triplet(l1, s):
        print("1")
    else:
        print('0')
