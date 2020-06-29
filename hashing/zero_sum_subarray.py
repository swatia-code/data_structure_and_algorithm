'''
PROBLEM STATEMENT
-----------------
You are given an array of integers. You need to print the total count of sub-arrays having their sum equal to 0

Input:
First line of the input contains an integer T denoting the number of test cases. Each test case consists of two lines. First line of each test case contains an Integer N denoting the size of the array, and the second line contains N space separated integers.

Output:
For each test case, in a new line, print the total number of subarrays whose sum is equal to 0.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:    
1 <= T <= 100
1 <= N <= 107
-1010 <= Ai <= 1010

Example:
Input:
2
6
0 0 5 5 0 0
10
6  -1 -3 4 -2 2 4 6 -12 -7
Output:
6
4

Explanation:
Testcase 1: There are 6 subarrays present whose sum is zero. The starting and ending indices are:
(0,0) (1,1) (0,1) (4,4) (5,5) (4,5)
Testcase 2: There are 4 subarrays present whose sum is zero. The starting and ending indices are:
(1,3) (4,5) (1,5) (5,8)

LOGIC
-----
Maintain sum of elements encountered so far in a variable (say sum).
If current sum is 0, we found a subarray starting from index 0 and ending at index current index
Check if current sum exists in the hash table or not.
If current sum already exists in the hash table then it indicates that this sum was the sum of some sub-array elements arr[0]…arr[i] and now the same sum is obtained for the current sub-array arr[0]…arr[j] which means that the sum of the sub-array arr[i+1]…arr[j] must be 0.
Insert current sum into the hash table

SOURCE
------
geeksforgeeks

CODE
----
'''
def zero_subarray(l):
    sum_freq = dict()
    
    sum = 0
    res = list()
    
    for i in range(len(l)):
        lis = list()
        sum += l[i]
        
        if sum == 0:
            res.append((0, i))
            
        if sum in sum_freq:
            lis = sum_freq[sum]
            for ele in lis:
                res.append((ele+1, i))
            
        lis.append(i)
        sum_freq[sum] = lis
            
    return res
    
t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    res = zero_subarray(l)
    print(len(res))
