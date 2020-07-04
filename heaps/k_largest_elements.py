'''
PROBLEM STATEMENT
-----------------
Given an array of N positive integers, print k largest elements from the array.  The output elements should be printed in decreasing order.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N and k, N is the size of array and K is the largest elements to be returned. The second line of each test case contains N input C[i].

Output:
Print the k largest element in descending order.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100
K ≤ N
1 ≤ C[i] ≤ 1000

Example:
Input:
2
5 2
12 5 787 1 23
7 3
1 23 12 9 30 2 50

Output:
787 23
50 30 23

Explanation:
Testcase 1: 1st largest element in the array is 787 and second largest is 23.
Testcase 2: 3 Largest element in the array are 50, 30 and 23.

LOGIC
-----
This method is mainly an optimization of method 1. Instead of using temp[] array, use Min Heap.

1) Build a Min Heap MH of the first k elements (arr[0] to arr[k-1]) of the given array. O(k)

2) For each element, after the kth element (arr[k] to arr[n-1]), compare it with root of MH.
……a) If the element is greater than the root then make it root and call heapify for MH
……b) Else ignore it.
// The step 2 is O((n-k)*logk)

3) Finally, MH has k largest elements and root of the MH is the kth largest element.

Time Complexity: O(k + (n-k)Logk) without sorted output. If sorted output is needed then O(k + (n-k)Logk + kLogk)


SOURCE
------
geeksforgeeks

CODE
----
'''
import heapq
def k_largest_element(l1, k):
    temp = list()
    for i in range(k):
        temp.append(l1[i])
        
        
    heapq.heapify(temp)
    
    for i in range(k,len(l1)):
        if l1[i] > temp[0]:
            heapq.heappop(temp)
            heapq.heappush(temp, l1[i])
      
    temp.sort(reverse=True)      
    for ele in temp:
        print(ele, end=" ")
    
t = int(input())
for _ in range(t):
    l = [int(x) for x in input().split()]
    k = l[1]
    l1 = [int(x) for x in input().split()]
    k_largest_element(l1, k)
    print()
