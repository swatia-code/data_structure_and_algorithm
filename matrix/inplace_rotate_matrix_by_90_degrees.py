'''
PROBLEM STATEMENT
-----------------
Given a square matrix mat[][] of size N x N. The task is to rotate it by 90 degrees in anti-clockwise direction without using any extra space.

Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines. The first line of each test case consists of an integer N, where N is the size of the square matrix.The second line of each test case contains N x N space separated values of the matrix mat.

Output:
Corresponding to each test case, in a new line, print the rotated array.

Constraints:
1 ≤ T ≤ 50
1 ≤ N ≤ 50
1 <= mat[][] <= 100

Example:
Input:
2
3
1 2 3 4 5 6 7 8 9
2
5 7 10 9
Output:
3 6 9 2 5 8 1 4 7
7 9 5 10

Explanation:
Testcase 1: Matrix is as below:
1 2 3
4 5 6
7 8 9

Rotating it by 90 degrees in anticlockwise directions will result as below matrix:
3 6 9
2 5 8
1 4 7

LOGIC
-----
There is N/2 squares or cycles in a matrix of side N. Process a square one at a time. Run a loop to traverse the matrix a cycle at a time, i.e loop from 0 to N/2 – 1, loop counter is i
Consider elements in group of 4 in current square, rotate the 4 elements at a time. So the number of such groups in a cycle is N – 2*i.
So run a loop in each cycle from x to N – x – 1, loop counter is y
The elements in the current group is (x, y), (y, N-1-x), (N-1-x, N-1-y), (N-1-y, x), now rotate the these 4 elements, i.e (x, y) <- (y, N-1-x), (y, N-1-x)<- (N-1-x, N-1-y), (N-1-x, N-1-y)<- (N-1-y, x), (N-1-y, x)<- (x, y)
Print the matrix.

SOURCE
------
geeksforgeeks

CODE
----
'''
def rotate_mat(mat, n):
    
    for x in range(0, n//2):
        for y in range(x, n - x - 1):
            temp = mat[x][y]
            mat[x][y] = mat[y][n - 1 -x]
            mat[y][n - 1 - x] = mat[n - 1 -x][n - 1 - y]
            mat[n - 1 - x][n - 1 - y] = mat[n - 1 -y][x]
            mat[n - 1 - y][x] = temp
            
    for row in mat:
        for ele in row:
            print(ele, end = ' ')

t = int(input())
for _ in range(t):
    n = int(input())
    s = [int(x) for x in input().split()]
    start = 0
    end = n 
    mat = list()
    
    for i in range(n):
        mat.append(s[start:end])
        start += n
        end += n
        
    rotate_mat(mat, n)
    print()
