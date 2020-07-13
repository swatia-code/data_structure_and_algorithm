'''
PROBLEM STATEMENT
-----------------
Given an array arr[] of N non-negative integers representing height of blocks at index i as Ai where the width of each block is 1. Compute how much water can be trapped in between blocks after raining.
Structure is like below:
|  |
|_|
We can trap 2 units of water in the middle gap.



Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. Each test case contains an integer N denoting the size of the array, followed by N space separated numbers to be stored in array.

Output:
Output the total unit of water trapped in between the blocks.

Constraints:
1 <= T <= 100
3 <= N <= 107
0 <= Ai <= 108

Example:
Input:
2
4
7 4 0 9
3
6 9 9

Output:
10
0

Explanation:
Testcase 1: Water trapped by block of height 4 is 3 units, block of height 0 is 7 units. So, total unit of water trapped is 10 units.

LOGIC
-----
The idea is to traverse every array element and find the highest bars on left and right sides. Take the smaller of two heights. The difference between the smaller height and height of the current element is the amount of water that can be stored in this array element.To make this efficient one must pre-compute the highest bar on the left and right of every bar in linear time. Then use these pre-computed values to find the amount of water in every array element.
Create two array left and right of size n. create a variable max_ = INT_MIN.
Run one loop from start to end. In each iteration update max_ as max_ = max(max_, arr[i]) and also assign left[i] = max_
Update max_ = INT_MIN.
Run another loop from end to start. In each iteration update max_ as max_ = max(max_, arr[i]) and also assign right[i] = max_
Traverse the array from start to end.
The amount of water that will be stored in this column is min(a,b) – array[i],(where a = left[i] and b = right[i]) add this value to total amount of water stored
Print the total amount of water stored.

SOURCE
------
geeksforgeeks

CODE
----
'''
def trap_water(l, n):
    
    left = list()
    right = list()
    
    left.append(l[0])
    for ele in l[1:]:
        left.append(max(left[-1], ele))
        
    right.append(l[-1])
    for i in range(n - 2, -1, -1):
        right.append(max(right[-1], l[i]))
        
    water = 0
    for i in range(n):
        water += (min(left[i], right[n - i - 1]) - l[i])
        
    return water

t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    print(trap_water(l, n))
