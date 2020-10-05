'''
PROBLEM STATEMENT
-----------------
Given a sequence A of size N, find the length of the longest increasing subsequence from a given sequence .
The longest increasing subsequence means to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.

Note: Duplicate numbers are not counted as increasing subsequence.

Input:
The first line contains an integer T, depicting total number of test cases. Then following T lines contains an integer N depicting the size of array and next line followed by the value of array.

Output:
For each testcase, in a new line, print the Max length of the subsequence in a separate line.

Constraints:
1 ≤ T ≤ 100
0 ≤ N ≤ 1000
0 ≤ A[i] ≤ 300

Example:
Input:
2
16
0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15
6
5 8 3 7 9 1

Output:
6
3

Explanation:
Testcase 2: Longest increasing subsequence is of size 3 with elements (there are many subsequence, but listing one of them): 5 7 9.

LOGIC
-----

Then, L(i) can be recursively written as:

L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
L(i) = 1, if no such j exists.
To find the LIS for a given array, we need to return max(L(i)) where 0 < i < n.

Formally, the length of the longest increasing subsequence ending at index i, will be 1 greater than the maximum of lengths of all longest increasing subsequences ending at indices before i, where arr[j] < arr[i] (j < i). Thus, we see the LIS problem satisfies the optimal substructure property as the main problem can be solved using solutions to subproblems. 
We can see that there are many subproblems in the above recursive solution which are solved again and again. So this problem has Overlapping Substructure property and recomputation of same subproblems can be avoided by either using Memoization or Tabulation.

SOURCE
------
geeksforgeeks

CODE
----
'''
def longest_increasing_subsequence(l, n):
    
    lis = list()
    
    for i in range(n):
        lis.append(1)
        
    for i in range(1, n):
        for j in range(i):
            if l[i] > l[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                
    ans = 1
    for i in range(n):
        ans = max(ans, lis[i])
        
    return ans
    

t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    print(longest_increasing_subsequence(l, n))
