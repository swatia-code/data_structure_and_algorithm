"""
PROBLEM STATEMENT
-----------------
Given a number and its reverse. Find that number raised to the power of its own reverse.
Note: As answers can be very large, print the result modulo 109 + 7.

Example 1:

Input:
N = 2
Output: 4
Explanation: The reverse of 2 is 2
and after raising power of 2 by 2 
we get 4 which gives remainder as 
4 by dividing 1000000007.
Example 2:

Input:
N = 12
Output: 864354781
Explanation: The reverse of 12 is 21
and 1221 , when divided by 1000000007 
gives remainder as 864354781.
Your Task:
You don't need to read input or print anything. You just need to complete the function pow() that takes two parameters N and R denoting the input number and its reverse and returns power of (N to R)mod(109 + 7).

Expected Time Complexity: O(LogN).
Expected Auxiliary Space: O(LogN).

Constraints:
1 <= N <= 105

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
"""
MOD = (10 ** 9) + 7

def power(N,R):
    #Your code here
    if R == 0:
        return 1
        
    if R == 1:
        return N
        
    val = power(N, R // 2)
    
    if R % 2:
        return ((val % MOD) * (val % MOD) * (N % MOD)) % MOD if R > 0 else ((val % MOD) * (val % MOD) // (N % MOD)) % MOD
    else:
        return ((val % MOD) * (val % MOD)) % MOD
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        
        ans=power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
