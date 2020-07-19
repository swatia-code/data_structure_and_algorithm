'''
PROBLEM STATEMENT
-----------------
There are N stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top (order does matter).

Input:
The first line contains an integer 'T' denoting the total number of test cases. In each test cases, an integer N will be given.

Output:
For each testcase, in a new line, print number of possible ways to reach Nth stair. Answer your output % 10^9+7.

Constraints:
1<=T<=105
1<=N<=105

Example:
Input:
3
4
10
24
Output:
5
89
75025

LOGIC
-----
We can easily find the recursive nature in the above problem. The person can reach nth stair from either (n-1)th stair or from (n-2)th stair. Hence, for each stair n, we try to find out the number of ways to reach n-1th stair and n-2th stair and add them to give the answer for the nth stair. Therefore the expression for such an approach comes out to be :

ways(n) = ways(n-1) + ways(n-2)
The above expression is actually the expression for Fibonacci numbers, but there is one thing to notice, the value of ways(n) is equal to fibonacci(n+1).

ways(1) = fib(2) = 1
ways(2) = fib(3) = 2
ways(3) = fib(4) = 3

SOURCE
------
geeksforgeeks

CODE
----
'''
mod = pow(10,9) + 7
dp = [0 for i in range(100001)]

def n_stairs(n):
    
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = ((dp[i - 1] % mod) + (dp[i - 2] % mod)) % mod
        

t = int(input())
n_stairs(100000)
for _ in range(t):
    n = int(input())
    print(dp[n])
