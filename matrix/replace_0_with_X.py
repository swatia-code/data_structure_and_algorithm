"""
PROBLEM STATEMENT
-----------------
Given a matrix of size NxM where every element is either ‘O’ or ‘X’, replace ‘O’ with ‘X’ if surrounded by ‘X’. A ‘O’ (or a set of ‘O’) is considered to be by surrounded by ‘X’ if there are ‘X’ at locations just below, just above, just left and just right of it.

Examples:

Input: mat[N][M] =  {{'X', 'O', 'X', 'X', 'X', 'X'},
                     {'X', 'O', 'X', 'X', 'O', 'X'},
                     {'X', 'X', 'X', 'O', 'O', 'X'},
                     {'O', 'X', 'X', 'X', 'X', 'X'},
                     {'X', 'X', 'X', 'O', 'X', 'O'},
                     {'O', 'O', 'X', 'O', 'O', 'O'},
                    };
Output: mat[N][M] =  {{'X', 'O', 'X', 'X', 'X', 'X'},
                      {'X', 'O', 'X', 'X', 'X', 'X'},
                      {'X', 'X', 'X', 'X', 'X', 'X'},
                      {'O', 'X', 'X', 'X', 'X', 'X'},
                      {'X', 'X', 'X', 'O', 'X', 'O'},
                      {'O', 'O', 'X', 'O', 'O', 'O'},
                    };

Input: mat[N][M] =  {{'X', 'X', 'X', 'X'}
                     {'X', 'O', 'X', 'X'}
                     {'X', 'O', 'O', 'X'}
                     {'X', 'O', 'X', 'X'}
                     {'X', 'X', 'O', 'O'}
                    };
Input: mat[N][M] =  {{'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'O', 'O'}
                    };

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. The first line of each test case contains two integers N and M denoting the size of the matrix. Then in the next line are N*M space separated values of the matrix.

Output:
For each test case print the space separated values of the new matrix.

Constraints:
1<=T<=10
1<=mat[][]<=100
1<=n,m<=20

Example:
Input:
2
1 5
X O X O X 
3 3
X X X X O X X X X
Output:
X O X O X
X X X X X X X X X

LOGIC
----

SOURCE
------
geeksforgeeks

CODE
----
"""
#code
def floodFillUtil(mat, x, y, prevV, newV): 
  
    if (x < 0 or x >= M or y < 0 or y >= N): 
        return
  
    if (mat[x][y] != prevV): 
        return
  
    mat[x][y] = newV 
  
    floodFillUtil(mat, x + 1, y, prevV, newV) 
    floodFillUtil(mat, x - 1, y, prevV, newV) 
    floodFillUtil(mat, x, y + 1, prevV, newV) 
    floodFillUtil(mat, x, y - 1, prevV, newV) 

t = int(input())
for _ in range(t):
    l = [int(x) for x in input().split()]
    M, N = l[0], l[1]
    
    l = [x for x in input().split()]
    
    mat = list()
    start = 0
    
    for i in range(M):
        mat.append(l[start: start + N])
        start += N
        
    for i in range(M): 
        if (mat[i][0] == '-'): 
            floodFillUtil(mat, i, 0, '-', 'O') 
      
    # Right side 
    for i in range(M):  
        if (mat[i][N - 1] == '-'): 
            floodFillUtil(mat, i, N - 1, '-', 'O') 
      
    # Top side 
    for i in range(N):  
        if (mat[0][i] == '-'): 
            floodFillUtil(mat, 0, i, '-', 'O') 
      
    # Bottom side 
    for i in range(N):  
        if (mat[M - 1][i] == '-'): 
            floodFillUtil(mat, M - 1, i, '-', 'O') 
  
    # Step 3: Replace all '-' with 'X' 
    for i in range(M): 
        for j in range(N): 
            if (mat[i][j] == '-'): 
                mat[i][j] = 'X'
                
    for i in range(M):
        for j in range(N):
            print(mat[i][j], end = ' ')
    
    print()
