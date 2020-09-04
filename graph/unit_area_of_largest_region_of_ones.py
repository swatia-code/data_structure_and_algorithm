'''
PROBLEM STATEMENT
-----------------
Consider a matrix with N rows and M columns, where each cell contains either a ‘0’ or a ‘1’ and any cell containing a 1 is called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally. If one or more filled cells are connected, they form a region. The task is to find the unit area of the largest region.

Input:
The first line of input will be the number of testcases T, then T testcases follow. The first line of each testcase contains 2 space separated integers n and m. Then in the next line are the n x m inputs of the matrix A separated by space.

Output:
The output in the expected output will be the length of the largest region formed.

Constraints:
1 <= T <= 100
1 <= N, M <= 50
0 <= A[][] <= 1

Example:
Input:
2
3 3
1 1 0 0 0 1 1 0 1
1 3
1 1 1

Output:
4
3

Explanation:
Testcase 1: Matrix can be shown as follows:
1 1 0
0 0 1
1 0 1

Largest region of 1s in the above matrix is with total 4 1s (colored in Red).
 
LOGIC
-----
A cell in 2D matrix can be connected to at most 8 neighbours.
So in DFS, make recursive calls for 8 neighbours of that cell.
Keep a visited Hash-map to keep track of all visited cells.
Also keep track of the visited 1’s in every DFS and update maximum length region.

SOURCE
------
geeksforgeeks

CODE
----
'''
def is_safe(matrix, row, col, visited):
    
    ROW = len(matrix)
    COL = len(matrix[0])
    
    return (row >= 0 and row < ROW and col >= 0 and col < COL and matrix[row][col] and not visited[row][col])

def DFS(matrix, row, col, val, visited):
    
    rp = [-1,-1,-1,0,0,1,1,1]
    cp = [-1,0,1,-1,1,-1,0,1]
    
    visited[row][col] = 1
    
    for pos in range(8):
        if is_safe(matrix, row + rp[pos], col + cp[pos], visited):
            val[0] += 1
            DFS(matrix, row + rp[pos], col + cp[pos], val, visited)

def largest_area(matrix, row, col):
    
    visited = [[0 for j in range(col)]for i in range(row)]
    result = float('-inf')
    
    for i in range(row):
        for j in range(col):
            if matrix[i][j] and not visited[i][j]:
                val = [1]
                DFS(matrix, i, j, val, visited)
                result = max(result, val[0])
    
    return result

t = int(input())
for _ in range(t):
    l = [int(x) for x in input().split()]
    row = l[0]
    col = l[1]
    mat = [int(x) for x in input().split()]
    start_index = 0
    matrix = list()
    for i in range(row):
        matrix.append(mat[start_index:start_index + col])
        start_index += col
        
    print(largest_area(matrix, row, col))
