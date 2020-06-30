'''
PROBLEM STATEMENT
-----------------
Given two arrays A and B of equal size, the task is to find if given arrays are equal or not. Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.
Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow.  Each test case contains 3 lines of input. The first line contains an integer N denoting the size of the array. The second line contains element of array A[]. The third line contains elements of the array B[].

Output:
For each test case, print 1 if the arrays are equal else print 0.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N). 

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= A[],B[] <= 1018

Example:
Input:
2
5
1 2 5 4 0
2 4 5 0 1
3
1 2 5
2 4 15
Output:
1
0

Explanation:
Testcase1:
Input : A[] = {1, 2, 5, 4, 0}; B[] = {2, 4, 5, 0, 1}; Since all the array elements are same. So,
Output : 1
Testcase2:
Input : A[] = {1, 2, 5}; B[] = {2, 4, 15}; Since all the array elements are not same. So,
Output : 0

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
def is_equal(l1, l2):
    freq_1 = dict()
    freq_2 = dict()
    
    for ele in l1:
        if ele not in freq_1:
            freq_1[ele] = 1
        else:
            freq_1[ele] += 1
            
    for ele in l2:
        if ele not in freq_2:
            freq_2[ele] = 1
        else:
            freq_2[ele] += 1 
            
    for ele in freq_1:
        if ele in freq_2:
            if freq_1[ele] != freq_2[ele]:
                return False
        else:
            return False
            
    return True

t = int(input())
for _ in range(t):
    n = input()
    l1 = [int(x) for x in input().split()]
    l2 = [int(x) for x in input().split()]
    if is_equal(l1, l2):
        print('1')
    else:
        print('0')
