'''
PROBLEM STATEMENT
-----------------
Write a function to print Boundary Traversal of a binary tree. Boundary Traversal of a binary tree here means that you have to print boundary nodes of the binary tree Anti-Clockwise starting from the root.
Note: Boundary node means nodes present at the boundary of left subtree and nodes present at the right subtree also including leaf nodes.
For the below tree, the function should print 20 8 4 10 14 25 22 .
    
                         
 

 

 

 

 

 

 

 

 



 

 

Input :
The first line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denote node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output:
The function should print the Boundary traversal of the tree.

Your Task:
This is a function problem. You don't have to take input. Just complete the function printBoundary() that takes the root node as input and returns an array containing the boundary values in anti-clockwise.

Expected Time Complexity: O(N). 
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <=T<= 30
1 <= Number of nodes<= 105
1 <= Data of a node<= 105

Example:
Input:
2
1 2 3
10 20 30 40 60

Output:
1 2 3
10 20 40 60 30

Explanation:
Testcase 1:


The first test case represents a tree with 3 nodes and 2 edges where the root is 1, the left child of 1 is 2 and the right child of 1 is 3. And boundary traversal of this tree prints nodes as 1 2 3.



LOGIC
-----
We break the problem in 3 parts:
1. Print the left boundary in top-down manner.
2. Print all leaf nodes from left to right, which can again be sub-divided into two sub-parts:
…..2.1 Print all leaf nodes of left sub-tree from left to right.
…..2.2 Print all leaf nodes of right subtree from left to right.
3. Print the right boundary in bottom-up manner.

We need to take care of one thing that nodes are not printed again. e.g. The left most node is also the leaf node of the tree.

SOURCE
------
geeksforgeeks

CODE
----
'''

def print_boundary_left(root, boundary):
    
    if root:
        if root.left:
            boundary.append(root.data)
            print_boundary_left(root.left, boundary)
            
        elif root.right:
            boundary.append(root.data)
            print_boundary_left(root.right, boundary)
            

def print_leaf_nodes(root, boundary):
    
    if root:
        print_leaf_nodes(root.left, boundary)
        
        if root.left is None and root.right is None:
            boundary.append(root.data)
            
        print_leaf_nodes(root.right, boundary)
         
         
def print_boundary_right(root, boundary):
    
    if root:
        if root.right:
            print_boundary_right(root.right, boundary)
            boundary.append(root.data)
            
        elif root.left:
            print_boundary_right(root.left, boundary)
            boundary.append(root.data)
   

def print_boundary_helper(root, boundary):
    
    if root:
        boundary.append(root.data)
        
    #look for the left side
    print_boundary_left(root.left, boundary)
    
    #printing leaf nodes
    print_leaf_nodes(root.left, boundary)
    print_leaf_nodes(root.right, boundary)
    
    #print the right side
    print_boundary_right(root.right, boundary)

def printBoundaryView(root):
    # Code here
    boundary = list()
    print_boundary_helper(root, boundary)
        
    return boundary

import sys
sys.setrecursionlimit(100000)
#Contributed by Sudarshan Sharma
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
        res = printBoundaryView(root)
        for i in res:
            print (i, end = " ")
        print('')


