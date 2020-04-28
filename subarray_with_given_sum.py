"""
PROBLEM STATEMENT
-----------------
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15

LOGIC
-----
If all the elements are positive and if a subarray has sum greater than the given sum then there is no possibility that adding elements to current subarray the sum will be the given sum. Approach is similar to that of sliding window.

SOURCE
------
geeksforgeeks

CODE
----
"""

def subarray_with_sum(li,sum):
    curr_sum = li[0]
    start = 0
    i = 1
    while i <= len(li):
        
        while (curr_sum > sum and start<i-1):
            curr_sum -= li[start]
            start += 1
            
        if curr_sum == sum :
            print(start+1,i)
            return
        
        if i<n:
            curr_sum +=li[i]
        
        i+=1
        
    print('-1')
    return

t = int(input())
for i in range(t):
    l = [int(x) for x in input().split()]
    n = l[0]
    sum = l[1]
    li = [int(x) for x in input().split()]
    subarray_with_sum(li,sum)
    
