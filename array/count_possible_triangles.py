"""
PROBLEM STATEMENT
-----------------
Given an unsorted array arr[] of positive integers. Find the number of triangles that can be formed with three different array elements as lengths of three sides of triangles. 

Example 1:

Input: 
3
3 5 4

Output: 
1

Explanation: 
A triangle is possible 
with all the elements 5, 3 and 4.
Example 2:

Input: 
5
6 4 9 7 8

Output: 
10

Explanation: 
There are 10 triangles
possible  with the given elements like
(6,4,9), (6,7,8),...

Your Task: This is a function problem. You only need to complete the function findNumberOfTriangles() that takes arr[] and N as input parameters and returns the count of total possible triangles.

Expected Time Complexity: O(N2).
Expected Space Complexity: O(1).

LOGIC
-----
Approach: First sort the array, and run a nested loop, fix an index and then try to fix an upper and lower index within which we can use all the lengths to form a triangle with that fixed index.
Algorithm:
Sort the array and then take three variables l, r and i, pointing to start, end-1 and array element starting from end of the array.
Traverse the array from end (n-1 to 1), and for each iteration keep the value of l = 0 and r = i-1
Now if a triangle can be formed using arr[l] and arr[r] then triangles can obviously formed
from a[l+1], a[l+2]…..a[r-1], arr[r] and a[i], because the array is sorted , which can be directly calculated using (r-l). and then decrement the value of r and continue the loop till l is less than r
If triangle cannot be formed using arr[l] and arr[r] then increment the value of r and continue the loop till l is less than r
So the overall complexity of iterating
through all array elements reduces.

SOURCE
------
geeksforgeeks

CODE
----
"""

class Solution:
    def findNumberOfTriangles(ob, arr, n):
        #code here
        count = 0
        arr.sort()
        
        for i in range(n - 1, 0, -1):
            l = 0
            r = i - 1
            while (l < r):
                if arr[l] + arr[r] > arr[i]:
                    count += (r - l)
                    r -= 1
                else:
                    l += 1
                    
        return count


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findNumberOfTriangles(arr,n))

# } Driver Code Ends
