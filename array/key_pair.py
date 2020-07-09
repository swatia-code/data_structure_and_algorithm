'''
PROBLEM STATEMENT
-----------------
Given an array A of N positive integers and another number X. Determine whether or not there exist two elements in A whose sum is exactly X.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N and X, N is the size of array. The second line of each test case contains N integers representing array elements A[i].

Output:
Print "Yes" if there exist two elements in A whose sum is exactly X, else "No" (without quotes).

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 105
1 ≤ A[i] ≤ 105

Example:
Input:
2
6 16
1 4 45 6 10 8
5 10
1 2 4 3 6

Output:
Yes
Yes

Explanation:
Testcases 1: 10 and 6 are numbers making a pair whose sum is equal to 16.

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
def key_pair(l, sum):
    freq = dict()
    
    for ele in l:
        if ele not in freq:
            freq[ele] = 1
        else:
            freq[ele] += 1
            
    for ele in l:
        if sum - ele in freq:
            if sum - ele == ele and freq[ele]>1:
                return True
            elif sum - ele != ele:
                return True
                
    return False


t = int(input())
for _ in range(t):
    l = [int(x) for x in input().split()]
    sum = l[1]
    l = [int(x) for x in input().split()]
    if key_pair(l, sum):
        print("Yes")
    else:
        print("No")
