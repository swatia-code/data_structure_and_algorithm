'''
PROBLEM STATEMENT
-----------------
Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.

Input:
The first line contains an integer 'T' denoting the total number of test cases. Then T testcases follow. Each testcases contains two lines of input. The first line denotes the size of the array N. The second lines contains the elements of the array A separated by spaces.

Output: 
For each testcase, print the sorted array.

Constraints:
1 <= T <= 500
1 <= N <= 106
0 <= Ai <= 2

Example:
Input :
2
5
0 2 1 2 0
3
0 1 0

Output:
0 0 1 2 2
0 0 1

Explanation:
Testcase 1: After segragating the 0s, 1s and 2s, we have 0 0 1 2 2 which shown in the output.


LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
def sort_array(n, l):
    
    freq = dict()
    
    for ele in l:
        if ele not in freq:
            freq[ele] = 1
        else:
            freq[ele] += 1
            
    res = list()
    for key in sorted(freq):
        val = freq[key]
        for i in range(val):
            res.append(key)
            
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    res = sort_array(n, l)
    for ele in res:
        print(ele, end= " ")
        
    print()
