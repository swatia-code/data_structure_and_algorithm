'''
PROBLEM STATEMENT
-----------------
Given two sorted linked lists consisting of N and M nodes respectively. The task is to merge both of the list (in-place) and return head of the merged list.
Note: It is strongly recommended to do merging in-place using O(1) extra space.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains N and M, and next two line contains N and M sorted elements in two lines for each.

Output:
For each testcase, print the merged list in sorted form.

User Task:
The task is to complete the function sortedMerge() which takes references to the heads of two linked lists as the arguments and returns the head of merged linked list.

Expected Time Complexity : O(n+m)
Expected Auxilliary Space : O(1)

Constraints:
1 <= T <= 100
1 <= N, M <= 104
1 <= Node's data <= 105

Example:
Input:
2
4 3
5 10 15 40 
2 3 20
2 2
1 1
2 4 
Output:
2 3 5 10 15 20 40
1 1 2 4

Explanation:
Testcase 1: After merging the two linked lists, we have merged list as 2, 3, 5, 10, 15, 20, 40.
Testcase 2: After merging the given two linked list , we have 1, 1, 2, 4 as output.
 
LOGIC
-----
Traverse the list from start to end.
If the head node of second list lies in between two node of the first list, insert it there and make the next node of second list as the head. Continue this until there is no node left in both lists, i.e. both the lists are traversed.
If the first list has reached end while traversing, point the next node to the head of second list.

SOURCE
------
geeksforgeeks

CODE
----
'''
def merge_util(h1, h2):
    if h1.next is None:
        h1.next = h2
        return h1
        
    curr_1 = h1
    next_1 = h1.next
    curr_2 = h2
    next_2 = h2.next
    
    while (next_1 is not None) and (curr_2 is not None):
        if (curr_2.data >= curr_1.data) and (curr_2.data <= next_1.data):
            next_2 = curr_2.next
            curr_1.next = curr_2
            curr_2.next = next_1
            
            curr_1 = curr_2
            curr_2 = next_2
            
        else:
            if next_1.next:
                next_1 = next_1.next
                curr_1 = curr_1.next
                
            else:
                next_1.next = curr_2
                return h1
                
    return h1
    
def sortedMerge(head_A, head_B):
    if head_A is None:
        return head_B
    if head_B is None:
        return head_A
        
    if head_A.data < head_B.data:
        return merge_util(head_A, head_B)
    else:
        return merge_util(head_B, head_A)

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node
        
# prints the elements of linked list
def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        n,m = map(int, input().strip().split())
        
        a = LinkedList() # create a new linked list 'a'.
        b = LinkedList() # create a new linked list 'b'.
        
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        
        for x in nodes_a:
            a.append(x)
        
        for x in nodes_b:
            b.append(x)
        
        printList(sortedMerge(a.head,b.head))

