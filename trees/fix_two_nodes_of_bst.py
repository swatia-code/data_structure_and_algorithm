'''
PROBLEM STATEMENT
-----------------
Two of the nodes of a Binary Search Tree (BST) are swapped. Fix (or correct) the BST by swapping them back. Do not change the structure of the tree.

Note: It is guaranteed than the given input will form BST, except for 2 nodes that will be wrong.

Example 1:

Input:
       10
     /    \
    5      8
   / \
  2   20
Output: 1
Explanation:
 
Example 2:

Input:
         11
       /    \
      3      17
       \    /
        4  10
Output: 1
Your Task:
You don't need to take any input. Just complete the function correctBst() that takes root node as parameter. The function should return the root of corrected BST. BST will then be checked by driver code and 0 or 1 will be printed.

Expected Time Complexity : O(n)

Expected Auxiliary Space : O(1)

Constraints:
1 <= Number of nodes <= 1000

LOGIC
-----
The inorder traversal of a BST produces a sorted array. So a simple method is to store inorder traversal of the input tree in an auxiliary array. Sort the auxiliary array. Finally, insert the auxiliary array elements back to the BST, keeping the structure of the BST same. The time complexity of this method is O(nLogn) and the auxiliary space needed is O(n).
We can solve this in O(n) time and with a single traversal of the given BST. Since inorder traversal of BST is always a sorted array, the problem can be reduced to a problem where two elements of a sorted array are swapped. There are two cases that we need to handle:
1. The swapped nodes are not adjacent in the inorder traversal of the BST. 

 For example, Nodes 5 and 25 are swapped in {3 5 7 8 10 15 20 25}. 
 The inorder traversal of the given tree is 3 25 7 8 10 15 20 5 
If we observe carefully, during inorder traversal, we find node 7 is smaller than the previous visited node 25. Here save the context of node 25 (previous node). Again, we find that node 5 is smaller than the previous node 20. This time, we save the context of node 5 (the current node ). Finally, swap the two node’s values.
2. The swapped nodes are adjacent in the inorder traversal of BST.

  For example, Nodes 7 and 8 are swapped in {3 5 7 8 10 15 20 25}. 
  The inorder traversal of the given tree is 3 5 8 7 10 15 20 25 
Unlike case #1, here only one point exists where a node value is smaller than the previous node value. e.g. node 7 is smaller than node 8. 
How to Solve? We will maintain three-pointers, first, middle, and last. When we find the first point where the current node value is smaller than the previous node value, we update the first with the previous node & the middle with the current node. When we find the second point where the current node value is smaller than the previous node value, we update the last with the current node. In the case of #2, we will never find the second point. So, the last pointer will not be updated. After processing, if the last node value is null, then two swapped nodes of BST are adjacent. 

SOURCE
------
geeksforgeeks

CODE
----
'''

def correct_bst_helper(root, first, middle, last, prev):
    
    if root:
        correct_bst_helper(root.left, first, middle, last, prev)
        
        if (prev[0] and root.data < prev[0].data):
            if not(first[0]):
                first[0] = prev[0]
                middle[0] = root
            else:
                last[0] = root
            
        prev[0] = root
        
        correct_bst_helper(root.right, first, middle, last, prev)

def correctBST(root):
    # code here
    # swap the 2 incorrectly placed nodes
    # and return the root of tree
    
    first = [None]
    middle = [None]
    last = [None]
    prev = [None]
    
    correct_bst_helper(root, first, middle, last, prev)
    
   
    if (first[0] and last[0]):
        first[0].data, last[0].data = last[0].data, first[0].data
    elif (first[0] and middle[0]):
        first[0].data, middle[0].data = middle[0].data, first[0].data
        
        
    return root


#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

def isBST(n,lower,upper):
    if n is None:
        return True
    if n.data<=lower or n.data>=upper:
        return False
    return isBST(n.left,lower,n.data) and isBST(n.right,n.data,upper)

def compare(a,b,mismatch):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    
    if a.data != b.data:
        mismatch.append( (a.data,b.data) )
    
    return compare(a.left,b.left,mismatch) and compare(a.right,b.right,mismatch)

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        s=input()
        
        root = buildTree(s)
        duplicate = buildTree(s)
        
        root = correctBST(root)
        
        # check 1: is tree now a BST
        if not isBST(root,0,1000000000):
            print(0)
            continue
        
        # check 2: comparing with duplicate tree
        
        mismatch = []
        # a list to store data of mismatching nodes
        
        if not compare(root, duplicate, mismatch):
            # false output from this function indicates change in tree structure
            print(0)
        
        if len(mismatch)!=2 or mismatch[0][0]!=mismatch[1][1] or mismatch[0][1]!=mismatch[1][0]:
            print(0)
        else:
            print(1)

# } Driver Code Ends

