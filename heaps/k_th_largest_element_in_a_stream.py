"""
PROBLEM STATEMENT
-----------------
Given an input stream of n integers, find the kth largest element for each element in the stream.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two lines. The first line of each test case contains two space separated integers k and n . Then in the next line are n space separated values of the array.

Output:
For each test case, in a new line, print the space separated values denoting the kth largest element at each insertion, if the kth largest element at a particular insertion in the stream doesn't exist print -1.

Constraints:
1 <= T <= 100
1 <= K <= n
1 <= n <= 106
1 <= stream[] <= 105

Example:
Input:
2
4 6
1 2 3 4 5 6
1 2
3 4

Output:
-1 -1 -1 1 2 3
3 4 

Explanation:
Testcase1:
k = 4
For 1, the 4th largest element doesn't exist so we print -1.
For 2, the 4th largest element doesn't exist so we print -1.
For 3, the 4th largest element doesn't exist so we print -1.
For 4, the 4th largest element is 1 {1, 2, 3, 4}
For 5, the 4th largest element is 2 {2, 3, 4 ,5}
for 6, the 4th largest element is 3 {3, 4, 5}
 

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
"""
#code
import heapq

def k_th_largest_number(l, k):
    if len(l) < k:
        return -1
        
    for i in range(k - 1):
        print(-1, end =' ')
    heap = l[:k]
    heapq.heapify(heap)
    print(heap[0], end=' ')
    end = k
    
    while end < len(l):
        if l[end] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, l[end])
        end += 1
        print(heap[0], end=' ')
            

t = int(input())
for _ in range(t):
    num = [int(x) for x in input().split()]
    k = num[0]
    n = num[1]
    l = [int(x) for x in input().split()]
    k_th_largest_number(l, k)
    print()
