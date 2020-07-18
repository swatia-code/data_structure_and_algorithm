'''
PROBLEM STATEMENT
-----------------
Given a Matrix consisting of 0s and 1s. Find the number of islands of connected 1s present in the matrix. 
Note: A 1 is said to be connected if it has another 1 around it (either of the 8 directions).

Input:
The first line of input will be the number of testcases T, then T test cases follow. The first line of each testcase contains two space separated integers N and M. Then in the next line are the NxM inputs of the matrix A separated by space .

Output:
For each testcase in a new line, print the number of islands present.

Your Task:
You don't need to read input or print anything. Your task is to complete the function findIslands() which takes the matrix A and its dimensions N and M as inputs and returns the number of islands of connected 1s present in the matrix. A 1 is said to be connected if it has another 1 around it (either of the 8 directions).

Expected Time Complexity: O(N*M).
Expected Auxiliary Space: O(N*M).

Constraints:
1 <= T <= 100
1 <= N, M <= 100
0 <= A[i][j] <= 1

Example(To be used only for expected output) :
Input
2
3 3
1 1 0 0 0 1 1 0 1
4 4
1 1 0 0 0 0 1 0 0 0 0 1 0 1 0 0

Output
2
2

Explanation:
Testcase 1: The graph will look like
1 1 0
0 0 1
1 0 1
Here, two islands will be formed
First island will be formed by elements {A[0][0] ,  A[0][1], A[1][2], A[2][2]}
Second island will be formed by {A[2][0]}.
Testcase 2: The graph will look like
1 1 0 0
0 0 1 0
0 0 0 1
0 1 0 0
Here, two islands will be formed
First island will be formed by elements {A[0][0] ,  A[0][1], A[1][2], A[2][3]}
Second island will be formed by {A[3][1]}.


LOGIC
-----
This is a variation of the standard problem: “Counting the number of connected components in an undirected graph”.
A connected component of an undirected graph is a subgraph in which every two vertices are connected to each other by a path(s), and which is connected to no other vertices outside the subgraph.
A graph where all vertices are connected with each other has exactly one connected component, consisting of the whole graph. Such a graph with only one connected component is called a Strongly Connected Graph.

The problem can be easily solved by applying DFS() on each component. In each DFS() call, a component or a sub-graph is visited. We will call DFS on the next un-visited component. The number of calls to DFS() gives the number of connected components. BFS can also be used.

SOURCE
------
geeksforgeeks

CODE
----
'''
import sys
sys.setrecursionlimit(100000)

def isSafe(i, j, visited, A, N, M): 
    return (i >= 0 and i < N and j >= 0 and j < M and not visited[i][j] and A[i][j])
        

def DFS(i, j, visited, A, N, M):
    rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
    colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    visited[i][j] = True
    
    for k in range(8):
        if isSafe(i + rowNbr[k], j + colNbr[k], visited, A, N, M):
            DFS(i + rowNbr[k], j + colNbr[k], visited, A, N, M)
        

def findIslands(A, N, M):
    #code here
    visited = [[False for j in range(M)]for i in range(N)] 
    
    count = 0
    
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and A[i][j] == 1:
                DFS(i, j, visited, A, N, M) 
                count += 1
                
    return count

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n,m = map(int,input().strip().split())
        cell_info = list(map(int,input().strip().split()))
        a = []
        k = 0 
        for i in range(n):
            row_i = []
            for j in range(m):
                row_i.append(cell_info[k])
                k+=1
            a.append(row_i)
        print(findIslands(a,n,m))
