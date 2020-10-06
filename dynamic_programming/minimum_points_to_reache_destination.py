'''
PROBLEM STATEMENT
-----------------
Given a grid of size M*N with each cell consisting of an integer which represents points. We can move across a cell only if we have positive points. Whenever we pass through a cell, points in that cell are added to our overall points, the task is to find minimum initial points to reach cell (m-1, n-1) from (0, 0) by following these certain set of rules :
 
1. From a cell (i, j) we can move to (i + 1, j) or (i, j + 1).
2. We cannot move from (i, j) if your overall points at (i, j) are <= 0.
3. We have to reach at (n-1, m-1) with minimum positive points i.e., > 0.

Example 1:

Input: M = 3, N = 3 
       arr[][] = {{-2,-3,3}, 
                  {-5,-10,1}, 
                  {10,30,-5}}; 

Output: 7
Explanation: 7 is the minimum value to
reach the destination with positive
throughout the path. Below is the path.
(0,0) -> (0,1) -> (0,2) -> (1, 2) -> (2, 2)
We start from (0, 0) with 7, we reach
(0, 1) with 5, (0, 2) with 2, (1, 2)
with 5, (2, 2) with and finally we have
1 point (we needed greater than 0 points
at the end).
Example 2:
Input: M = 3, N = 2
       arr[][] = {{2,3}, 
                  {5,10}, 
                  {10,30}}; 
Output: 1
Explanation: Take any path, all of them 
are positive. So, required one point 
at the start

Your Task:  
You don't need to read input or print anything. Complete the function minPoints() which takes N, M and 2-d vector as input parameters and returns the integer value

Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(N*M)

Constraints:
1 ≤ N ≤ 103

LOGIC
-----
Given a grid with each cell consisting of positive, negative or no points i.e, zero points. We can move across a cell only if we have positive points ( > 0 ). Whenever we pass through a cell, points in that cell are added to our overall points. We need to find minimum initial points to reach cell (m-1, n-1) from (0, 0).

Constraints :

From a cell (i, j) we can move to (i+1, j) or (i, j+1).
We cannot move from (i, j) if your overall points at (i, j) is <= 0.
We have to reach at (n-1, m-1) with minimum positive points i.e., > 0.
Example:

Input: points[m][n] = { {-2, -3,   3}, 
                        {-5, -10,  1}, 
                        {10,  30, -5} 
                      };
Output: 7
Explanation: 
7 is the minimum value to reach destination with 
positive throughout the path. Below is the path.

(0,0) -> (0,1) -> (0,2) -> (1, 2) -> (2, 2)

We start from (0, 0) with 7, we reach(0, 1) 
with 5, (0, 2) with 2, (1, 2) with 5, (2, 2)
with and finally we have 1 point (we needed 
greater than 0 points at the end). 

At the first look, this problem looks similar Max/Min Cost Path, but maximum overall points gained will not guarantee the minimum initial points. Also, it is compulsory in the current problem that the points never drops to zero or below. For instance, Suppose following two paths exists from source to destination cell.

We can solve this problem through bottom-up table filling dynamic programing technique.

To begin with, we should maintain a 2D array dp of the same size as the grid, where dp[i][j] represents the minimum points that guarantees the continuation of the journey to destination before entering the cell (i, j). It’s but obvious that dp[0][0] is our final solution. Hence, for this problem, we need to fill the table from the bottom right corner to left top.
Now, let us decide minimum points needed to leave cell (i, j) (remember we are moving from bottom to up). There are only two paths to choose: (i+1, j) and (i, j+1). Of course we will choose the cell that the player can finish the rest of his journey with a smaller initial points. Therefore we have: min_Points_on_exit = min(dp[i+1][j], dp[i][j+1])
Now we know how to compute min_Points_on_exit, but we need to fill the table dp[][] to get the solution in dp[0][0].

How to compute dp[i][j]?
     The value of dp[i][j] can be written as below.

dp[i][j] = max(min_Points_on_exit – points[i][j], 1)


Let us see how above expression covers all cases.

If points[i][j] == 0, then nothing is gained in this cell; the player can leave the cell with the same points as he enters the room with, i.e. dp[i][j] = min_Points_on_exit.
If points[i][j] < 0, then the player must have points greater than min_Points_on_exit before entering (i, j) in order to compensate for the points lost in this cell. The minimum amount of compensation is " – points[i][j] ", so we have dp[i][j] = min_Points_on_exit – points[i][j].
If points[i][j] > 0, then the player could enter (i, j) with points as little as min_Points_on_exit – points[i][j]. since he could gain “points[i][j]” points in this cell. However, the value of min_Points_on_exit – points[i][j] might drop to 0 or below in this situation. When this happens, we must clip the value to 1 in order to make sure dp[i][j] stays positive:
dp[i][j] = max(min_Points_on_exit – points[i][j], 1).
Finally return dp[0][0] which is our answer.


SOURCE
------
geeksforgeeks

CODE
----
'''
class Solution:
	def minPoints(self, points, m, n):
		# code here
		dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
		if points[m - 1][n - 1] > 0: 
		    dp[m - 1][n - 1] = 1
		else: 
		    dp[m - 1][n - 1] = abs(points[m - 1][n - 1]) + 1
		    
		for i in range (m - 2, -1, -1): 
		    dp[i][n - 1] = max(dp[i + 1][n - 1] - points[i][n - 1], 1) 
		for i in range (n - 2, -1, -1): 
		    dp[m - 1][i] = max(dp[m - 1][i + 1] - points[m - 1][i], 1)
		
		for i in range(m - 2, -1, -1): 
		    for j in range(n - 2, -1, -1): 
		        min_points_on_exit = min(dp[i + 1][j], dp[i][j + 1]) 
		        dp[i][j] = max(min_points_on_exit - points[i][j], 1) 
		        
		return dp[0][0]

