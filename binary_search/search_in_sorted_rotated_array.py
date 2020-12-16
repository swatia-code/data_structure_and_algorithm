'''
PROBLEM STATEMENT
-----------------
Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element K. The task is to find the index of the given element K in the array A.

Input:
The first line of the input contains an integer T, denoting the total number of test cases. Then T test cases follow. Each test case consists of three lines. First line of each test case contains an integer N denoting the size of the given array. Second line of each test case contains N space separated integers denoting the elements of the array A. Third line of each test case contains an integer K denoting the element to be searched in the array.

Output:
Corresponding to each test case, output the index of the element found in the array.  If element is not present, then output -1.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
0 ≤ Ai ≤ 108
1 ≤ K ≤ 108

Example:
Input:
3
9
5 6 7 8 9 10 1 2 3
10
3
3 1 2
1
4
3 5 1 2
6

Output:
5
1
-1

Explanation:
Testcase 1: 10 is found at index 5.


LOGIC
-----

SOURCE
-------
geeksforgeeks

CODE
----
'''
#code
def search(l, m):
    n = len(l)
    ans = -1
    if m == l[n -1]:
        return n - 1
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end)//2
        # if key is in greater region and mid in lower region
        if m > l[n - 1] and l[mid] < l[n - 1]:
            end = mid - 1
        # if key is in lower region and mid in higher region
        elif m < l[n - 1] and l[mid] > l[n - 1]:
            start = mid + 1
        #if both are in same region
        else:
            if m > l[mid]:
                start = mid + 1
            elif m < l[mid]:
                end = mid - 1
            else:
                ans = mid
                break
    return ans

t = int(input())
for _ in range(t):
	n = int(input())
	l = [int(x) for x in input().split()]
	m = int(input())
	print(search(l, m))
