"""
PROBLEM STATEMENT
-----------------
Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y co-ordinates of two points: the left top corner and the right bottom corner of the rectangle. Two rectangles sharing a side are considered overlapping.

Note : It may be assumed that the rectangles are parallel to the coordinate axis.

rectanglesOverlap

Input:
The first integer T denotes the number of testcases. For every test case, there are 2 lines of input. The first line consists of 4 integers: denoting the co-ordinates of the 2 points of the first rectangle. The first integer denotes the x co-ordinate and the second integer denotes the y co-ordinate of the left topmost corner of the first rectangle. The next two integers are the x and y co-ordinates of right bottom corner. Similarly, the second line denotes the cordinates of the two points of the second rectangle in similar fashion.

Output:
For each testcase, output (either 1 or 0) denoting whether the 2 rectangles are overlapping. 1 denotes the rectangles overlap whereas 0 denotes the rectangles do not overlap.

Constraints:
1 <= T <= 10
-104 <= x, y <= 104

Example:
Input:
2
0 10 10 0
5 5 15 0
0 2 1 1
-2 -3 0 2

Output:
1
0

Explanation:
Testcase 1: According to the coordinates given as input ,two rectangles formed overlap with each other and thus answer returns 1.

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
"""

if __name__ != '__init__':
    t = int(input())
    for _ in range(t):
        line = list(map(int, input().split()))
        # print(line)
        R1_LTx = line[0]
        R1_LTy = line[1]
        R1_RBx = line[2]
        R1_RBy = line[3]
        line = list(map(int, input().split()))
        # print(line)
        R2_LTx = line[0]
        R2_LTy = line[1]
        R2_RBx = line[2]
        R2_RBy = line[3]

        if R1_RBy > R2_LTy or R2_RBy > R1_LTy:
            print(0)
        elif R1_LTx > R2_RBx or R2_LTx > R1_RBx:
            print(0)
        else:
            print(1)
