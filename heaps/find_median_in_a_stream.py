'''
PROBLEM STATEMENT
-----------------
Given an input stream of N integers. The task is to insert these numbers into a new stream and find the median of the stream formed by each insertion of X to the new stream.

Input:
The first line of input contains an integer N denoting the number of elements in the stream. Then the next N lines contains integer x denoting the number to be inserted into the stream.
Output:
For each element added to the stream print the floor of the new median in a new line.
 
Constraints:
1 <= N <= 106
1 <= x <= 106
 
Example:
Input:
4
5
15
1 
3
Output:
5
10
5
4
 
Explanation:
Testcase 1:
Flow in stream : 5, 15, 1, 3
5 goes to stream --> median 5 (5)
15 goes to stream --> median 10 (5, 15)
1 goes to stream --> median 5 (5, 15, 1)
3 goes to stream --> median 4 (5, 15, 1, 3)

LOGIC
-----
Median can be defined as the element in the data set which separates the higher half of the data sample from the lower half. In other words we can get the median element as, when the input size is odd, we take the middle element of sorted data. If the input size is even, we pick average of middle two elements in sorted stream.
Create two heaps. One max heap to maintain elements of lower half and one min heap to maintain elements of higher half at any point of time..
Take initial value of median as 0.
For every newly read element, insert it into either max heap or min heap and calculate the median based on the following conditions:
If the size of max heap is greater than size of min heap and the element is less than previous median then pop the top element from max heap and insert into min heap and insert the new element to max heap else insert the new element to min heap. Calculate the new median as average of top of elements of both max and min heap.
If the size of max heap is less than size of min heap and the element is greater than previous median then pop the top element from min heap and insert into max heap and insert the new element to min heap else insert the new element to max heap. Calculate the new median as average of top of elements of both max and min heap.
If the size of both heaps are same. Then check if current is less than previous median or not. If the current element is less than previous median then insert it to max heap and new median will be equal to top element of max heap. If the current element is greater than previous median then insert it to min heap and new median will be equal to top element of min heap.

SOURCE
------
geeksforgeeks

CODE
----
'''
from heapq import heappush, heappop
def balance_heaps(mx_heap, mn_heap):
    while abs(len(mx_heap) - len(mn_heap)) > 1:
        if len(mx_heap) > len(mn_heap):
            heappush(mn_heap, -1 * heappop(mx_heap))
        else:
            heappush(mx_heap, -1 * heappop(mn_heap))


def main():
    t = int(input().strip())
    init = int(input().strip())
    mx_heap = [-1 * init]
    mn_heap = []
    print(init)
    for _ in range(t - 1):
        e = int(input().strip())
        if e < (-1 * mx_heap[0]):
            heappush(mx_heap, -1 * e)
        else:
            heappush(mn_heap, e)
        balance_heaps(mx_heap, mn_heap)
        if len(mx_heap) > len(mn_heap):
            print(-1 * mx_heap[0])
        elif len(mx_heap) < len(mn_heap):
            print(mn_heap[0])
        else:
            print((-1 * mx_heap[0] + mn_heap[0]) // 2)
        

main()
