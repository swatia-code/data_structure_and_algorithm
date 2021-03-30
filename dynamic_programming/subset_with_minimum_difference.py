"""
PROBLEM STATEMENT
-----------------
Given an integer array arr of size N, the task is to divide it into two sets S1 and S2 such that the absolute
 difference between their sums is minimum and find the minimum difference

Example 1:

Input: N = 4, arr[] = {1, 6, 11, 5}
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12
Subset2 = {11}, sum of Subset2 = 11
Example 2:
Input: N = 2, arr[] = {1, 4}
Output: 3
Explanation:
Subset1 = {1}, sum of Subset1 = 1
Subset2 = {4}, sum of Subset2 = 4

Your Task:
You don't need to read input or print anything. Complete the function minDifference() which takes N and array arr
 as input parameters and returns the integer value

Expected Time Complexity: O(N*|sum of array elements|)
Expected Auxiliary Space: O(N*|sum of array elements|)

Constraints:
1 ≤ N*|sum of array elements| ≤ 106

TIME COMPLEXITY
----------------
O(N * sum of array elements)

CODE
----
"""


class Solution:
    def minDiffernce(self, arr, n):
        # code here
        s1_val = list()
        S = sum(arr)

        def subset_sum():
            dp = [[False for _ in range(S + 1)] for _ in range(n + 1)]

            for i in range(n + 1):
                dp[i][0] = True

            for i in range(1, n + 1):
                for j in range(S + 1):
                    if arr[i - 1] <= j:
                        dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j]

            for i in range(S // 2 + 1):
                if dp[n][i]:
                    s1_val.append(i)

        subset_sum()
        res = float('inf')
        for i in range(len(s1_val)):
            res = min(res, S - 2 * s1_val[i])

        return res
