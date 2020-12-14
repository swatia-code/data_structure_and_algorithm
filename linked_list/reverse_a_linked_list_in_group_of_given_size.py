'''
PROBLEM STATEMENT
-----------------
Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list.

Example 1:

Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4
Output: 4 2 2 1 8 7 6 5
Example 2:

Input:
LinkedList: 1->2->3->4->5
K = 3
Output: 3 2 1 5 4
Your Task:
The task is to complete the function reverse() which should reverse the linked list in group of size k and return the head of the modified linked list.

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(1)

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
def reverse(head, k):
    # Code here
    prev = None
    new = None
    temp = head
    count = 0
    
    while temp and count < k:
        new = temp.next 
        temp.next = prev
        prev = temp
        temp = new
        count += 1
        
    if new:
        head.next = reverse(new, k)
        
    return prev
