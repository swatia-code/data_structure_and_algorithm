'''
PROBLEM STATEMENT
-----------------
Given a BST and an integer K. Find the Kth Smallest element in the BST. 

Input:
The first line of input contains the number of test cases T. For each test case, there will two lines. The first line of input is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denote node values, and a character “N” denotes NULL child.

For example:
 
For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Second-line is an integer represents K

Output:
For each test case, the output will be the kth smallest element of BST. If no such element exists then print -1.

Your Task:
You don't need to read input or print anything. Your task is to complete the function KthSmallestElement() which takes the root of the BST and integer K as inputs and return the Kth smallest element in the BST.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1<=T<=10
1<=N<=100000


Example(To be used only for expected output):
Input:
2
2 1 3
2
2 1 3
5
Output:
2
-1

LOGIC
-----
store the tree element in inorder traversal as it will give elements in ascending order. Return k th element in array formed.

SOURCE
------
geeksforgeeks

CODE
----
'''
def inorder(root, l):
    
    if root:
        inorder(root.left, l)
        l.append(root.data)
        inorder(root.right, l)
        
# Return the Kth smallest element in the given BST 
def KthSmallestElement(root, K): 
    #code here.
    l = list()
    inorder(root, l)
    
    if len(l) < K:
        return -1
    else:
        return l[K - 1]

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
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        k1=int(input())
        print(KthSmallestElement(root, k1))
