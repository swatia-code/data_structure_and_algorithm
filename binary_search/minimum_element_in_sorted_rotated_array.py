'''
PROBLEM STATEMENT
-----------------
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines. The first line of each test case consists of an integer N, where N is the size of array.
The second line of each test case contains N space separated integers denoting array elements.

Output:
Corresponding to each test case, in a new line, print the minimum element in the array.

Constraints:

1 ≤ T ≤ 200
1 ≤ N ≤ 500
1 ≤ A[i] ≤ 1000

Example:

Input
2
5
4 5 1 2 3
6
10 20 30 40 50 5 7

Output
1
5

LOGIC
-----
he minimum element is the only element whose previous is greater than it. If there is no previous element, then there is no rotation (first element is minimum). We check this condition for middle element by comparing it with (mid-1)’th and (mid+1)’th elements.
If the minimum element is not at the middle (neither mid nor mid + 1), then minimum element lies in either left half or right half.
If middle element is smaller than last element, then the minimum element lies in left half
Else minimum element lies in right half.

SOURCE
------
geeksforgeeks

CODE
----
'''
def minimum_in_sorted_rotated_array(l, n):
	start = 0 # starting index of array
	end = n - 1 # last index of array
	ans = l[n - 1]
	while start <= end:
		
		mid = start + (end - start) // 2
		#when mid ele is less than last element
		if l[mid] < l[n - 1]:
			ans = l[mid]
			end = mid - 1
		else:
			start = mid + 1
			
	return ans

t = int(input())
for _ in range(t):
	n = int(input())
	l = [int(x) for x in input().split()]
	res = minimum_in_sorted_rotated_array(l, n)
	print(res)

