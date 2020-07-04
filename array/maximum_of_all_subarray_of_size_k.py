'''
PROBLEM STATEMENT
-----------------
Given an array A and an integer K. Find the maximum for each and every contiguous subarray of size K.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case contains a single integer N denoting the size of array and the size of subarray K. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum for every subarray of size k.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
1 ≤ K ≤ N
0 ≤ A[i] <= 107

Example:
Input:
2
9 3
1 2 3 1 4 5 2 3 6
10 4
8 5 10 7 9 4 15 12 90 13

Output:
3 3 4 5 5 5 6
10 10 10 15 15 90 90

Explanation:
Testcase 1: Starting from first subarray of size k = 3, we have 3 as maximum. Moving the window forward, maximum element are as 3, 4, 5, 5, 5 and 6.

LOGIC
-----
Approach1:
Create a Deque, Qi of capacity k, that stores only useful elements of current window of k elements. An element is useful if it is in current window and is greater than all other elements on left side of it in current window. Process all array elements one by one and maintain Qi to contain useful elements of current window and these useful elements are maintained in sorted order. The element at front of the Qi is the largest and element at rear of Qi is the smallest of current window. 
Create a deque to store k elements.
Run a loop and insert first k elements in the deque. While inserting the element if the element at the back of the queue is smaller than the current element remove all those elements and then insert the element.
Now, run a loop from k to end of the array.
Print the front element of the array
Remove the element from the front of the queue if they are out of the current window.
Insert the next element in the deque. While inserting the element if the element at the back of the queue is smaller than the current element remove all those elements and then insert the element.
Print the maximum element of the last window.
Compelxity Analysis:
Time Complexity: O(n).
It seems more than O(n) at first look. It can be observed that every element of array is added and removed at most once. So there are total 2n operations.
Auxiliary Space: O(k).
Elements stored in the dequeue take O(k) space.

approach 2:
In the above-mentioned methods, one of them was using AVL tree. This approach is very similar to that approach. The difference is that instead of using the AVL tree, Max-Heap will be used in this approach. The elements of the current window will be stored in the Max-Heap and the maximum element or the root will be printed in each iteration.
Max-heap is a suitable data structure as it provides constant-time retrieval and logarithmic time removal of both the minimum and maximum elements in it, i.e. it takes constant time to find the maximum element and insertion and deletion takes log n time.
Algorithm:
Pick first k elements and create a max heap of size k.
Perform heapify and print the root element.
Store the next and last element from the array
Run a loop from k – 1 to n
Replace the value of element which is got out of the window with new element which came inside the window.
Perform heapify.
Print the root of the Heap.
Complexity Analysis:
Time Complexity: O(n * k).
The time complexity of steps 4(a) is O(k), 4(b) is O(Log(k)) and it is in a loop that runs (n – k + 1) times. Hence, the time complexity of the complete algorithm is O((k + Log(k)) * n) i.e. O(n * k).
Space Complexity: O(k).
To store the elements in Heap O(k) space is used.

SOURCE
------
geeksforgeeks

CODE
----
'''
import heapq
from collections import deque


def maximum_of_subarray(l1, k):
    n = len(l1)
    Q = deque()
    
    for i in range(k):
        while Q and l1[i] >= l1[Q[-1]]:
            Q.pop()
        Q.append(i)
        
    for i in range(k,n):
        print(l1[Q[0]], end = " ")
        
        while Q and Q[0] <= i-k:
            Q.popleft()
            
        while Q and l1[i] >= l1[Q[-1]]:
            Q.pop()
        Q.append(i)
        
    print(l1[Q[0]])
    
def maximum_of_subarray_2(l, k):
    n = len(l)
    heap = l[:k]
    heapq._heapify_max(heap)
    print(heap[0], end = ' ')
    
    i = 0
    last = l[i]
    
    for j in range(k,n):
        next = l[j]
        heap[heap.index(last)] = next
        
        heapq._heapify_max(heap)
        
        print(heap[0], end= " ")
        
        i += 1
        last = l[i]

t = int(input())
for _ in range(t):
    l = [int(x) for x in input().split()]
    k = l[-1]
    l1 = [int(x) for x in input().split()]
    maximum_of_subarray(l1, k)
