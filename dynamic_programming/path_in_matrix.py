'''
PROBLEM STATEMENT
-----------------
Given a N X N  matrix Matrix[N][N] of positive integers.  There are only three possible moves from a cell Matrix[r][c].

1. Matrix[r+1][c]

2. Matrix[r+1][c-1]

3. Matrix[r+1][c+1]

Starting from any column in row 0, return the largest sum of any of the paths up to row N-1.

Input:
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the order of matrix. Next line contains N*N integers denoting the elements of the matrix in row-major form.

Output:
Output the largest sum of any of the paths starting from any cell of row 0 to any cell of row N-1. Print the output of each test case in a new line.

Constraints:
1<=T<=20
2<=N<=20
1<=Matrix[i][j]<=1000 (for all 1<=i<=N && 1<=j<=N)

Example:

Input:
1
2
348 391 618 193

Output:
1009

Explanation: In the sample test case, the path leading to maximum possible sum is 391->618.  (391 + 618 = 1009)

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''

def recurrence(mat ,i ,j ,n ,dp):
    if (i >= n) or (j < 0) or (j >= n):
        return 0
        
    if i == n - 1:
        return mat[i][j]
        
    if(dp[i][j]!=-1):
        return dp[i][j]
        
    a = recurrence(mat ,i + 1 ,j - 1 ,n ,dp )
    b = recurrence(mat ,i + 1 ,j ,n ,dp)
    c = recurrence(mat ,i + 1 ,j + 1 ,n ,dp)
    
    dp[i][j] = mat[i][j] + max(a,max(b,c))
    
    return dp[i][j]
    
def path_in_matrix(mat, n):
    
    max_ans = 0
    dp = [[-1 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        ans = recurrence(mat, 0 ,i ,n ,dp)
        max_ans = max(max_ans, ans)
        
    return max_ans

t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    mat = list()
    start = 0
    for i in range(n):
        mat.append(l[start: start + n])
        start += n
        
    print(path_in_matrix(mat, n))
