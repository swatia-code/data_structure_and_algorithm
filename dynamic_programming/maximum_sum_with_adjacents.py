'''
PROBLEM STATEMENT
-----------------
Given an array Arr of size N containing positive integers. Find the maximum sum of a subsequence such that no two numbers in the sequence should be adjacent in the array.

Example 1:

Input:
N = 6
Arr[] = {5, 5, 10, 100, 10, 5}
Output: 110
Explanation: If you take indices 0, 3
and 5, then Arr[0]+Arr[3]+Arr[5] =
5+100+5 = 110.
Example 2:

Input:
N = 4
Arr[] = {3, 2, 7, 10}
Output: 13
Explanation: 3 and 10 forms a non
continuous  subsequence with maximum
sum.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findMaxSum() which takes the array of integers arr and n as parameters and returns an integer denoting the answer.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 106
1 ≤ Arri ≤ 107

or


There are n houses build in a line, each of which contains some value in it. A thief is going to steal the maximal value of these houses, but he can’t steal in two adjacent houses because the owner of the stolen houses will tell his two neighbours left and right side. What is the maximum stolen value?

Examples:

Input: hval[] = {6, 7, 1, 3, 8, 2, 4}
Output: 19

Explanation: The thief will steal 6, 1, 8 and 4 from the house.

Input: hval[] = {5, 3, 4, 11, 2}
Output: 16

Explanation: Thief will steal 5 and 11


LOGIC
-----
Algorithm:
Create an extra space dp, DP array to store the sub-problems.
Tackle some basic cases, if the length of the array is 0, print 0, if the length of the array is 1, print the first element, if the length of the array is 2, print maximum of two elements.
Update dp[0] as array[0] and dp[1] as maximum of array[0] and array[1]
Traverse the array from the second element to the end of array.
For every index, update dp[i] as maximum of dp[i-2] + array[i] and dp[i-1], this step defines the two cases, if an element is selected then the previous element cannot be selected and if an element is not selected then the previous element can be selected.
Print the value dp[n-1]

SOURCE
------
geeksforgeeks

CODE
----
'''
class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
		if n == 0:
		    return 0
		
		if n == 1:
		    return arr[0]
		    
		if n == 2:
		    return max(arr[0],arr[1])
		    
		sum_array = [0] * n
		sum_array[0] = arr[0]
		sum_array[1] = max(arr[0], arr[1])
		for i in range(2, n):
		    sum_array[i] = max(sum_array[i - 2] + arr[i], sum_array[i - 1])
		return sum_array[n - 1]
