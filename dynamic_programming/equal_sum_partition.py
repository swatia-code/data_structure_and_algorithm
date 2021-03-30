"""
PROBLEM STATEMENT
-----------------
Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements
in both parts is the same.

Example 1:

Input: N = 4
arr = {1, 5, 11, 5}
Output: YES
Explaination:
The two parts are {1, 5, 5} and {11}.
Example 2:

Input: N = 3
arr = {1, 3, 5}
Output: NO
Explaination: This array can never be
partitioned into two such parts.

Your Task:
You do not need to read input or print anything. Your task is to complete the function equalPartition()
 which takes the value N and the array as input parameters and returns 1 if the partition is possible. Otherwise,
  returns 0.


Expected Time Complexity: O(N*sum of elements)
Expected Auxiliary Space: O(N*sum of elements)


TIME COMPLEXITY
---------------
O(N * SUM OF ELEMENTS)

CODE
----
"""


class Solution:
    def equalPartition(self, N, arr):
        # code here
        def subset_sum(arr, N, S):
            dp = [[False for _ in range(S + 1)] for _ in range(N + 1)]

            for i in range(N + 1):
                dp[i][0] = True

            for i in range(1, N + 1):
                for j in range(1, S + 1):
                    if arr[i - 1] <= j:
                        dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j]

            return dp[N][S]

        s = sum(arr)
        if s & 1:
            return False
        return subset_sum(arr, N, s // 2)
