'''
PROBLEM STATEMENT
-----------------
There are ‘p’ balls of type P, ‘q’ balls of type Q and ‘r’ balls of type R. Using the balls we want to create a straight line such that no two balls of same type are adjacent.

Input:
First line of input contains number of test cases T. Each line of test case contains number of balls of each type seperated by a single space.

Output:
Number of ways to arrange balls are displayed and 0 is displayed if there are no ways.

Constraints:
1 <= T <= 30
1 <= p,q,r <= 9

Example:
Input:
2
2 2 2
1 1 1
Output:
30
6

LOGIC
-----
The naive solution to this problem is a recursive solution. We recursively call for three cases
1) Last ball to be placed is of type P
2) Last ball to be placed is of type Q
3) Last ball to be placed is of type R

We can observe that there are many subproblems being solved again and again so the problem can be solved using Dynamic Programming (DP). We can easily make memoization solution to this problem.

SOURCE
------
geeksforgeeks

CODE
----
'''
MAX = 10

dp = [[[[-1] * 4 for i in range(MAX)]for j in range(MAX)]for k in range(MAX)]

def count_ways(p, q, r, last):
    if (p < 0 or q < 0 or r < 0):
        return 0 
    if (p == 1 and q == 0 and r == 0 and last == 0):
        return 1
    if (p == 0 and q == 1 and r == 0 and last == 1):
        return 1
    if (p == 0 and q == 0 and r == 1 and last == 2):
        return 1
    
    if (dp[p][q][r][last] != -1):
        return dp[p][q][r][last]
        
    if (last == 0):
        dp[p][q][r][last] = (count_ways(p - 1, q, r, 1) + count_ways(p - 1, q, r, 2))
    elif (last == 1):
        dp[p][q][r][last] = (count_ways(p, q - 1, r, 0) + count_ways(p, q - 1, r, 2))
    else:
        dp[p][q][r][last] = (count_ways(p, q, r - 1, 0) + count_ways(p, q, r - 1, 1))
        
    return dp[p][q][r][last] 


def arrange_balls(p, q, r):
    return count_ways(p, q, r, 0) + count_ways(p, q, r, 1) + count_ways(p, q, r, 2)

t = int(input())
for _ in range(t):
    l = [int(x) for x in input().split()]
    p = l[0]
    q = l[1]
    r = l[2]
    print(arrange_balls(p, q, r))
