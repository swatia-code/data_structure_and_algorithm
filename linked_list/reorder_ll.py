"""
PROBLEM STATEMENT
-----------------
Given a singly linked list: A0→A1→…→An-1→An, reorder it to: A0→An→A1→An-1→A2→An-2→…
For example: Given 1->2->3->4->5 its reorder is 1->5->2->4->3.

Note: It is recommended do this in-place without altering the nodes' values.

Input:
First line of input contains number of testcases T. For each testcase, there will be two lines of input, first of which contains length of linked list and next line contains elements of the nodes of linked list.

Output:
Reorder it as explained above.

User Task:
The task is to complete the function reorderList() which should reorder the list as required.

Note: Try to solve without using any auxilliary space.

Constraints:
1 <= T <= 200
1 <= N <= 104

Example:
Input:

2
3
1 2 3
4
1 7 3 4

Output:
1 3 2
1 4 7 3

Explanation:
Testcase 2: After rearranging the given list as required, we have list as 1 -> 4 -> 7 -> 3.

LOGIC
-----
1.Brute force
i) Initialize current node as head.
ii) While next of current node is not null, do following:
	a) Find the last node, remove it from the end and insert it as next
	b) Move current to next to next of current 
Time complexity is O(n2)

2. Efficient Approach
i) Find the middle point using fast and slow pointer approach.
ii) Split the linked list into two halves using found middle point.
iii) Reverse the second half.
iv) Do alternate merge of firsta nd second halves

SOURCE
------
geeksforgeeks

CODE
----
"""

def reverse_list(head):
    prev = None
    curr = head
    temp = None
    
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        
    return prev
    

def reorderList(self):
    if (self.head==None or self.head.next==None):
        return
    # write code to reorder Nodes of Linked_List
    # Split the linked list in two halves
    fast = self.head
    slow = self.head
    temp = self.head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    #reverse second half
    head1 = reverse_list(slow.next)
    
    slow.next = None
    
    new_head = node(0)
    curr = new_head
    
    while temp or head1:
        if head:
            curr.next = temp
            temp = temp.next
            curr = curr.next
            
        if head1:
            curr.next = head1
            head1 = head1.next
            curr = curr.next
    
    new_head = new_head.next
    
    
    return new_head
#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    reorder_List = reorderList

    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp=tmp.next
        print()

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        lis.reorder_List()
        lis.printList()

# } Driver Code Ends
