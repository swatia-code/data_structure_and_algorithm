'''
PROBLEM STATEMENT
-----------------
Given an unsorted array Arr of N positive and negative numbers. Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.

Example 1:

Input: 
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output: 9 -2 4 -1 5 -5 0 -3 2
Example 2:

Input: 
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output: -5 5 -2 2 -8 4 7 1 8 0 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function rearrange() which takes the array of integers arr[] and n as parameters. You need to modify the array itself.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Note: Array should start with positive number.

Constraints:
1 ≤ N ≤ 107
-106 ≤ Arr[i] ≤ 107

LOGIC
-----
An array contains both positive and negative numbers in random order. Rearrange the array elements so that positive and negative numbers are placed alternatively. Number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array.

For example, if the input array is [-1, 2, -3, 4, 5, 6, -7, 8, 9], then the output should be [9, -7, 8, -3, 5, -1, 2, 4, 6]

Note: The partition process changes relative order of elements. I.e. the order of the appearance of elements is not maintained with this approach. See this for maintaining order of appearance of elements in this problem.

The solution is to first separate positive and negative numbers using partition process of QuickSort. In the partition process, consider 0 as value of pivot element so that all negative numbers are placed before positive numbers. Once negative and positive numbers are separated, we start from the first negative number and first positive number, and swap every alternate negative number with next positive number.

SOURCE
------
geeksforgeeks

CODE
----
'''
class Solution:
    def rearrange(self,arr, n):
        # code here
        i = -1
        for j in range(n):
            if arr[j] < 0:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
                
        pos = i + 1
        neg = 0
        
        while neg < pos and pos < n and arr[neg] < 0:
            arr[neg], arr[pos] = arr[pos], arr[neg]
            pos += 1
            neg += 2
            
            
        return arr
