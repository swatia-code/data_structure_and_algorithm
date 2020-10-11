'''
PROBLEM STATEMENT
-----------------
Given a matrix mat[][] of size N x M, where every row and column is sorted in increasing order, and a number X is given. The task is to find whether element X is present in the matrix or not.

Example 1:

Input:
N = 3
M = 3
mat[][]: 3 30 38 
         44 52 54 
         57 60 69
X = 62
Output:
0
Explanation: 62 is not present in the
matrix, so output is 0

Example 2:

Input:
N = 1
M = 6
mat[][] : 18 21 27 38 55 67
X = 55
Output:
1
Explanation: 55 is present in the
matrix at 5th cell.

Your Task:
You don't need to read input or print anything. You just have to complete the function matSearch() which takes a 2D matrix mat[][], its dimensions N and M and integer X as inputs and returns 1 if the element X is present in the matrix and 0 otherwise.

Expected Time Complexity: O(N+M).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N, M <= 30
1 <= mat[][] <= 100
1<= X <= 100

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
class Solution:
    def binary_search(self, l, start, end, X):
        while start <= end:
            mid = (start + end) // 2
            if l[mid] == X:
                return 1
            if l[mid] > X:
                end = mid - 1
            else:
                start = mid + 1
                
        return 0
        
    def matSearch(self,mat, N, M, X):
        for i in range(N):
            ans = 0
            if mat[i][0] <= X and X <= mat[i][M - 1]:
                ans = self.binary_search(mat[i], 0, M - 1, X)
                if ans == 1:
                    break
                
        return ans
