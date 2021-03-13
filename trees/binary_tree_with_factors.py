"""
PROBLEM STATEMET:
https://leetcode.com/problems/binary-trees-with-factors/

LOGIC:
Actually, let dp[i] be the number of ways to have a root node with value A[i].

Since in the above example we always have x < v and y < v, we can calculate the values of dp[i] in increasing order using dynamic programming.

For some root value A[i], let's try to find candidates for the children with values A[j] and A[i] / A[j] (so that evidently A[j] * (A[i] / A[j]) = A[i]). To do this quickly, we will need index which looks up this value: if A[k] = A[i] / A[j], then index[A[i] / A[j]] = k`.

After, we'll add all possible dp[j] * dp[k] (with j < i, k < i) to our answer dp[i]. In our Java implementation, we carefully used long so avoid overflow issues.

SOLUTION
"""
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()
        dp = [1] * len(arr)
        
        ind = {num: i for i, num in enumerate(arr)}
        
        for i, num in enumerate(arr):
            for j in range(i):
                if num % arr[j] == 0:
                    right_child = num / arr[j]
                    if right_child in ind:
                        dp[i] = ((dp[j] % MOD * dp[ind.get(right_child)] % MOD) % MOD + dp[i] % MOD) % MOD
                        
        val = 0
        
        for ele in dp:
            val = (val % MOD + ele % MOD) % MOD
            
        return val
