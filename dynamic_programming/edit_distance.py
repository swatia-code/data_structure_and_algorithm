"""
PROBLEM STATEMENT
-----------------
Given two strings s and t. Find the minimum number of operations that need to be performed on str1 to convert it to str2. The possible operations are:

Insert
Remove
Replace
 

Example 1:

Input: 
s = "geek", t = "gesek"
Output: 1
Explanation: One operation is required 
inserting 's' between two 'e's of str1.

Example 2:

Input : 
s = "gfg", t = "gfg"
Output: 
0
Explanation: Both strings are same.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function editDistance() which takes strings s and t as input parameters and returns the minimum number of operation required to make both strings equal. 

 

Expected Time Complexity: O(n2)
Expected Space Complexity: O(n2)
 

Constraints:
1 <= Length of both strings <= 100
Both the strings are in lowercase.


LOGIC
-----
The idea is process all characters one by one staring from either from left or right sides of both strings. 
Let us traverse from right corner, there are two possibilities for every pair of character being traversed.  

m: Length of str1 (first string)
n: Length of str2 (second string)
If last characters of two strings are same, nothing much to do. Ignore last characters and get count for remaining strings. So we recur for lengths m-1 and n-1.
Else (If last characters are not same), we consider all operations on ‘str1’, consider all three operations on last character of first string, recursively compute minimum cost for all three operations and take minimum of three values. 
Insert: Recur for m and n-1
Remove: Recur for m-1 and n
Replace: Recur for m-1 and n-1

The time complexity of above solution is exponential. In worst case, we may end up doing O(3m) operations. The worst case happens when none of characters of two strings match. Below is a recursive call diagram for worst case. 

We can see that many subproblems are solved, again and again, for example, eD(2, 2) is called three times. Since same suproblems are called again, this problem has Overlapping Subprolems property. So Edit Distance problem has both properties of a dynamic programming problem. Like other typical Dynamic Programming(DP) problems, recomputations of same subproblems can be avoided by constructing a temporary array that stores results of subproblems.

SOURCE
------
geeksforgeeks

CODE
----
"""
  class Solution:  
    def edit_distance_helper(self, m, n, str1, str2):
        dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
 
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j   
                elif j == 0:
                    dp[i][j] = i   
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
 
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                    dp[i-1][j],        # Remove
                                    dp[i-1][j-1])    # Replace
 
        return dp[m][n]
    
    
    def editDistance(self, s, t):
        # Code here
        return self.edit_distance_helper(len(s), len(t), s, t)
        
            
        

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution();
        ans = ob.editDistance(s, t)
        print(ans)
# } Driver Code Ends
