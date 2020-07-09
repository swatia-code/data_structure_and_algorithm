'''
PROBLEM STATEMENT
-----------------
Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

Example:
A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]

NOTE 1: If there is a tie, then compare with segment's length and return segment which has maximum length
NOTE 2: If there is still a tie, then return the segment with minimum starting index

Input:
The first line contains an integer T, depicting total number of test cases. 
Then following T lines contains an integer N depicting the size of array and next line followed by the value of array.

Output:
Print the Sub-array with maximum sum.

Constraints:
1 ≤ T ≤ 40
1 ≤ N ≤ 100
-100 ≤ A[i] ≤ 100

Example:
Input
2
3
1 2 3
2
-1  2
Output
1 2 3
2

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
def cal(arr,n):
    ind = []
    temp, final, pf = 0, 0, 0
    for i in range(n):
        if arr[i] > -1:
            temp += arr[i]
        if i == n - 1 or arr[i] < 0:
            if i == n - 1 and not (arr[i] < 0):
                i += 1
            if final == temp:
                ind.append([(i - pf), pf, i])
            elif final < temp:
                final = temp
                del ind[:]
                ind.append([(i - pf), pf, i])
            temp = 0
            pf = i + 1

    if len(ind) == 1:
        return ind[0][1], ind[0][2]
    else:
        ind = sorted(ind, reverse = True)
        le = ind[0][0]
        st = ind[0][1]
        en = ind[0][2]
        for i in ind:
            if i[0] == le and i[1] < st:
                st = i[1]
                en = i[2]
        return st, en
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    a, b = cal(arr, n)
    print(*arr[a : b])

