'''
PROBLEM STATEMENT
------------------
Given a sorted array, arr[] of N integers, and a value X. Find the K closest elements to X in arr[].
Keep the following points in mind:

If X is present in the array, then it need not be considered.
If there are two elements with the same difference with X, the greater element is given priority.
If sufficient elements are not present on the right side then take elements from left and vice versa.
 
Example 1:

Input:
N = 13
arr[] = {12, 16, 22, 30, 35, 39, 42, 
         45, 48, 50, 53, 55, 56}
K = 4, X = 35
Output: 30 39 42 45
Explanation: 
First closest element to 35 is 30.
Second closest element to 35 is 39.
Third closest element to 35 is 42.
And fourth closest element to 35 is 45.

Example 2:

Input:
N = 5
Arr[] = {1, 2, 3, 6, 10}
K = 3, X = 4
Output: 3 6 2
Explanation: 
First closest element is 3.
There are two elements 2 and 6 for which 
the difference with 4 is same i.e. 2.
So first take greatest number 6 
then the lower number 2.

Your Task:
You don't need to read input or print anything. Complete the function printKClosest() which takes arr[], n, k and x as input parameters and returns an array of integers containing the K closest elements to X in arr[].


Expected Time Complexity: O(logN + K)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 105
1 ≤ Arr[i] ≤ 106


LOGIC
-----
The idea is to use Binary Search to find the crossover point. Once we find index of crossover point, we can print k closest elements in O(k) time.

SOURCE
------
geeksforgeeks

CODE
----
'''
class Solution:
    def get_index(self, arr, n, x):
        if x >= arr[n - 1]:
            return n - 1
            
        elif x <= arr[0]:
            return 0
        
        start = 0
        end = n - 1
        
        while (start <= end):
            
            mid = start + (end - start) // 2
            
            if arr[mid] <= x and arr[mid + 1] > x:
                return mid
                
            elif arr[mid] < x:
                start = mid + 1
                
            else:
                end = mid - 1
                
        
    
    def printKClosest(self, arr, n, k, x):
        target_index = self.get_index(arr, n, x)
        
        if arr[target_index] == x:
            left_ind = target_index - 1
        else:
            left_ind = target_index
            
        right_ind = target_index + 1
        
        ans = list()
        count = 0
        
        while left_ind >= 0 and right_ind < len(arr) and count < k:
            if (x - arr[left_ind]) < (arr[right_ind] - x):
                ans.append(arr[left_ind])
                left_ind -= 1
            else:
                ans.append(arr[right_ind])
                right_ind += 1
                
            count += 1
            
        while count < k and  left_ind >= 0:
            ans.append(arr[left_ind])
            left_ind -= 1
            count += 1
            
        while count < k and  right_ind < len(arr):
            ans.append(arr[right_ind])
            right_ind += 1
            count += 1
        
        
        return ans
