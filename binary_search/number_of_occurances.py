'''
PROBLEM STATEMENT
-----------------
Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.

Example 1:

Input:
N = 7, X = 2
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 4
Explanation: 2 occurs 4 times in the
given array.
Example 2:

Input:
N = 7, X = 4
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 0
Explanation: 4 is not present in the
given array.
Your Task:
You don't need to read input or print anything. Your task is to complete the function count() which takes the array of integers arr, n and x as parameters and returns an integer denoting the answer.

Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
1 ≤ Arr[i] ≤ 106
1 ≤ X ≤ 106

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
class Solution:
    def _get_first_pos(self, arr, n, x):
        start = 0
        end = n - 1
        ans = -1
        
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] >= x:
                ans = mid
                end = mid - 1
            elif arr[mid] < x:
                start = mid + 1
                
        return ans
        
    def _get_last_pos(self, arr, n, x):
        start = 0
        end = n - 1
        ans = -1
        
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] <= x:
                ans = mid
                start = mid + 1
            elif arr[mid] > x:
                end = mid - 1
                
        return ans
        

    def count(self,arr, n, x):
        # code here
        first_position = self._get_first_pos(arr, n, x)
        last_position = self._get_last_pos(arr, n, x)
        
        if first_position != -1:
            return last_position - first_position + 1
            
        return 0
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends
