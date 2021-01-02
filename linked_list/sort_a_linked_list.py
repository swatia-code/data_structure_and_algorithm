"""
PROBLEM STATEMENT
-----------------
Given Pointer/Reference to the head of the linked list, the task is to Sort the given linked list using Merge Sort.
Note: If the length of linked list is odd, then the extra node should go in the first list while splitting.

Example 1:

Input:
N = 5
value[]  = {3,5,2,4,1}
Output: 1 2 3 4 5
Explanation: After sorting the given
linked list, the resultant matrix
will be 1->2->3->4->5.
Example 2:

Input:
N = 3
value[]  = {9,15,0}
Output: 0 9 15
Explanation: After sorting the given
linked list , resultant will be
0->9->15.
Your Task:
For C++ and Python: The task is to complete the function mergeSort() which sort the linked list using merge sort function.
For Java: The task is to complete the function mergeSort() and return the node which can be used to print the sorted linked list.

Expected Time Complexity: O(N*Log(N))
Expected Auxiliary Space: O(1)

Constraints:
1 <= T <= 100
1 <= N <= 105

LOGIC
-----
MergeSort(headRef)
1) If the head is NULL or there is only one element in the Linked List 
    then return.
2) Else divide the linked list into two halves.  
      FrontBackSplit(head, &a, &b); /* a and b are two halves */
3) Sort the two halves a and b.
      MergeSort(a);
      MergeSort(b);
4) Merge the sorted a and b (using SortedMerge() discussed here) 
   and update the head pointer using headRef.
     *headRef = SortedMerge(a, b);

SOURCE
------
geeksforgeeks

CODE
----
"""
def merge(head_a, head_b):
    result = None
    
    if head_a is None:
        return head_b

    if head_b is None:
        return head_a
        
    if head_a.data <= head_b.data:
        result = head_a
        result.next = merge(head_a.next, head_b)
    else:
        result = head_b
        result.next = merge(head_a, head_b.next)
        
    return result
    
def get_middle(head):
    if head is None:
        return head
    
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow

def mergeSort(head):
    '''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
    '''
    
    if head is None or head.next is None:
        return head
        
    middle_point = get_middle(head)
    second_head = middle_point.next
    
    middle_point.next = None
    
    left = mergeSort(head)
    right = mergeSort(second_head)
    
    sorted_list = merge(left, right)
    
    return sorted_list

