'''
PROBLEM STATEMENT
-----------------
You are given a Singly Linked List with N nodes where each node next pointing to its next node. You are also given M random pointers , where you will be given M number of pairs denoting two nodes a and b  i.e. a->arb = b.

ArbitLinked List1

Example 1:

Input:
N = 4, M = 
value = {1,2,3,4}
pairs = {{1,2},{2,4}}
Output: 1
Explanation: In this test case, there
re 4 nodes in linked list.  Among these
4 nodes,  2 nodes have arbit pointer
set, rest two nodes have arbit pointer
as NULL. Third line tells us the value
of four nodes. The fourth line gives the
information about arbitrary pointers.
The first node arbit pointer is set to
node 2.  The second node arbit pointer
is set to node 4.
Example 2:

Input:
N = 4, M = 2
value[] = {1,3,5,9}
pairs[] = {{1,1},{3,4}}
Output: 1
Explanation: In the given testcase ,
applying the method as stated in the
above example, the output will be 1.
Your Task:
The task is to complete the function copyList() which takes one argument the head of the linked list to be cloned and should return the head of the cloned linked list.
NOTE : If their is any node whose arbitrary pointer is not given then its by default null.

Expected Time Complexity : O(n)
Expected Auxilliary Space : O(1)

Constraints:
1 <= N <= 100
1 <= M <= N
1 <= a, b <= 100

LOGIC
-----
The idea is to use Hashing. Below is algorithm.
1. Traverse the original linked list and make a copy in terms of data.
2. Make a hash map of key value pair with original linked list node and copied linked list node.
3. Traverse the original linked list again and using the hash map adjust the next and random reference of cloned linked list nodes.

SOURCE
------
GEEKSFORGEEKS

CODE
----
'''
'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
'''

def copyList(head):
    '''
    param: head:  head of linkedList to copy
    return: the head of the copied linked list the #output will be 1 if successfully copied
    '''
    
    dictionary = dict()
    
    temp_head = head
    
    while temp_head is not None:
        n = Node(temp_head.data)
        dictionary[temp_head] = n
        temp_head = temp_head.next

    temp_head = head
    
    res_head = dictionary[temp_head]
    while temp_head is not None:
        n = dictionary[temp_head]
        if dictionary.get(temp_head.next):
            n.next = dictionary[temp_head.next]
        if dictionary.get(temp_head.arb):
            n.arb = dictionary[temp_head.arb]
        temp_head = temp_head.next
            
    return res_head

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
        
class LinkedList:
    def __init__(self):
        self.head = None

def insert(tail,data):
    tail.next=Node(data)
    return tail.next
    

def setarb(head,a,b):
    h=head
    i=1
    while i<a and h:
        h=h.next
        i+=1
    an=h
    
    h=head
    i=1
    while i<b and h:
        h=h.next
        i+=1
        
    if an:
        an.arb=h
        
def validation(head,res):
    
    while head and res:
        if id(head)==id(res):
            return
        
        #print(head.data,res.data,end=' ')
        if head.data != res.data:
            return
        
        if head.arb:
            if not res.arb:
                return
            
            #print(head.arb.data,res.arb.data)
            if head.arb.data != res.arb.data:
                return
            
        elif res.arb:
            return
        head=head.next
        res=res.next
        
    if not head and res:
        return
    elif head and not res:
        return
    
    return True


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n,m = list(map(int, input().strip().split()))
        nodes = list(map(int, input().strip().split()))
        aarb = list(map(int, input().strip().split()))
        ll=LinkedList()
        ll.head=Node(nodes[0])
        tail=ll.head
        
        for x in nodes[1:]:
            tail=insert(tail,x)
        
        for i in range(0,len(aarb),2):
            setarb(ll.head,aarb[i],aarb[i+1])
        
        res=copyList(ll.head)
        if validation(ll.head,res):
            print(1)
        else:
            print(0)
# } Driver Code Ends
