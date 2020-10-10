'''
PROBLEM STATEMENT
-----------------
Given an array of integers which is initially increasing and then decreasing, find the maximum value in the array.
Examples :

Input: arr[] = {8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1}
Output: 500

Input: arr[] = {1, 3, 50, 10, 9, 7, 6}
Output: 50

Corner case (No decreasing part)
Input: arr[] = {10, 20, 30, 40, 50}
Output: 50

Corner case (No increasing part)
Input: arr[] = {120, 100, 80, 20, 0}


LOGIC
-----
We can modify the standard Binary Search algorithm for the given type of arrays.
i) If the mid element is greater than both of its adjacent elements, then mid is the maximum.
ii) If mid element is greater than its next element and smaller than the previous element then maximum lies on left side of mid. Example array: {3, 50, 10, 9, 7, 6}
iii) If mid element is smaller than its next element and greater than the previous element then maximum lies on right side of mid. Example array: {2, 4, 6, 8, 10, 3, 1}

SOURCE
------
geeksforgeeks

CODE
----
'''
class Solution:


	def findNumber(self,arr, n, k):
	    start = 0
	    end = n - 1
	    if n == 1:
	        return arr[n - 1]
	    
	    if n == 2:
	        return max(arr[0], arr[1])
	    ans = arr[0]
	    
	    while start <= end:
	        mid = start + (end - start) // 2
	        if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:
	            return arr[mid]
	        elif arr[mid - 1] < arr[mid] and arr[mid] < arr[mid - 1]:
	            ans = arr[mid]
	            start = mid + 1
	        else:
	            end = mid - 1
	    return ans
