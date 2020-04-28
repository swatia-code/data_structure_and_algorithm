"""
PROBLEM STATEMENT
-----------------
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.

Constraints:
1 ≤ T ≤ 110
1 ≤ N ≤ 106
-107 ≤ A[i] <= 107

Example:
Input
2
5
1 2 3 -2 5
4
-1 -2 -3 -4
Output
9
-1

Explanation:
Testcase 1: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.

LOGIC
-----
Simple idea of Kadane's algorithm is to look for all positive contiguous segments of array. And keep track of maximum sum contiguous segment among all positive segments. Each time we get a positive sum coompare it with max_so_far and update it .

SOURCE
------
geeksforgeeks

CODE
----
"""

#code
def check_negative(li):
    for ele in li:
        if ele > 0:
            return False
    return True

def kadane(li):
    max_abs = 0
    max_ins = 0
    
    if check_negative(li):
        li.sort()
        return li[len(li)-1]
        
    for ele in li:
        max_ins += ele
        if max_ins<0:
            max_ins = 0
        else:
            if max_ins>max_abs:
                max_abs = max_ins
                
    return max_abs

t = int(input())
for i in range(t):
    n = input()
    li = [int(x) for x in input().split()]
    print(kadane(li))
