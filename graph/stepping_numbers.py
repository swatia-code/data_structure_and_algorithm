'''
PROBLEM STATEMENT
-----------------
A number is called stepping number if all adjacent digits have an absolute difference of 1, e.g. '321' is a Stepping Number while 421 is not. Given two integers n and m, find the count of all the stepping numbers in range [n, m].

Examples:

Input : n = 0, m = 21
Output : 13
Stepping no's are 0 1 2 3 4 5 6 7 8 9 10 12 21

Input : n = 10, m = 15
Output : 2
Stepping no's are 10, 12
Input:
The first line of the input contains an integer T, denoting the number of test cases. Then T test case follows. The only line of each test case contains two space separated integers denoting the values of n and m respectively.

Output:
For each test case in a new line print an integer denoting the number of stepping numbers in the range between n and m.

Constraints:
1<=T<=102
0<=N,M<=10^6

Example:
Input:
3
0 21
10 15
0 1
Output:
13
2
2

LOGIC
-----
The idea is to use a Breadth First Search/Depth First Search traversal.

How to build the graph?
Every node in the graph represents a stepping number; there will be a directed edge from a node U to V if V can be transformed from U. (U and V are Stepping Numbers) A Stepping Number V can be transformed from U in following manner.

lastDigit refers to the last digit of U (i.e. U % 10)
An adjacent number V can be:

U*10 + lastDigit + 1 (Neighbor A)
U*10 + lastDigit – 1 (Neighbor B)
By applying above operations a new digit is appended to U, it is either lastDigit-1 or lastDigit+1, so that the new number V formed from U is also a Stepping Number.
Therefore, every Node will have at most 2 neighboring Nodes.

Edge Cases: When the last digit of U is 0 or 9

Case 1: lastDigit is 0 : In this case only digit ‘1’ can be appended.
Case 2: lastDigit is 9 : In this case only digit ‘8’ can be appended.

What will be the source/starting Node?

Every single digit number is considered as a stepping Number, so bfs traversal for every digit will give all the stepping numbers starting from that digit.
Do a bfs/dfs traversal for all the numbers from [0,9].
Note: For node 0, no need to explore neighbors during BFS traversal since it will lead to 01, 012, 010 and these will be covered by the BFS traversal starting from node 1.

Example to find all the stepping numbers from 0 to 21

-> 0 is a stepping Number and it is in the range
   so display it.
-> 1 is a Stepping Number, find neighbors of 1 i.e.,
   10 and 12 and push them into the queue

How to get 10 and 12?
Here U is 1 and last Digit is also 1 
V = 10 + 0 = 10 ( Adding lastDigit - 1 )
V = 10 + 2 = 12 ( Adding lastDigit + 1 )

Then do the same for 10 and 12 this will result into
101, 123, 121 but these Numbers are out of range. 
Now any number transformed from 10 and 12 will result
into a number greater than 21 so no need to explore 
their neighbors.

-> 2 is a Stepping Number, find neighbors of 2 i.e. 
   21, 23.
-> 23 is out of range so it is not considered as a 
   Stepping Number (Or a neighbor of 2)

The other stepping numbers will be 3, 4, 5, 6, 7, 8, 9.


SOURCE
------
geeksforgeeks

CODE
----
'''
#code
def bfs(start, end, i, count):
    q = list()
    q.append(i)
    
    while len(q):
        num = q[0]
        q.pop(0)
        
        if num >= start and num <= end:
            count[0] += 1
            
        if num == 0 or num > end:
            continue
        
        last_digit = num % 10
        
        num_1 = (num * 10) + last_digit - 1
        num_2 = (num * 10) + last_digit + 1
        
        
        if last_digit == 0:
            q.append(num_2)
            
        elif last_digit == 9:
            q.append(num_1)
        
        else:
            q.append(num_1)
            q.append(num_2)
            

def stepping_numbers(n, m):
    
    count = [0]
    for i in range(10):
        bfs(n, m, i, count)
        
    return count[0]

t = int(input())
for _ in range(t):
    n, m = list(map(int,input().split()))
    print(stepping_numbers(n, m))
