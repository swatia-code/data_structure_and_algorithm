'''
PROBLEM STATEMENT
-----------------
Given a BST, modify it so that all greater values in the given BST are added to every node.

Input Format:

The first line of input contains the number of test cases T. Each test case contains a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denote node values, and a character “N” denotes NULL child.

For example:
 
For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output:
Print the inorder traversal of the modified BST.

Your Task:
You don't need to read input or print anything. Your task is to complete the function modify() which takes one argument: root of the BST. The function should contain the logic to modify the BST so that in the modified BST, every node has a value equal to the sum of its value in the original BST and values of all the elements larger than it in the original BST. Return the root of the modified BST.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(Height of the BST).

Constraints:
1<=T<=10
1<=N<=100000

Example:
Input:
2
50 30 70 20 40 60 80
2 1 5 N N 4 7

Output:
350 330 300 260 210 150 80
19 18 16 12 7
Explanation:

              50
           /      \
         30        70
        /   \      /  \
      20    40    60   80 

The above tree should be modified to following 

              260
           /      \
         330        150
        /   \       /  \
      350   300    210   80


LOGIC
-----
reverse of inorder traversal and adding value to parent node.

SOURCE
------
geeksfogeeks

CODE
----
'''
def modify_helper(root, s):
    
    if root == None:
        return
    
    modify_helper(root.right, s)
    
    s[0] = s[0] + root.data
    root.data = s[0]
    
    modify_helper(root.left, s)

# modify the BST and return its root
def modify(root):
    #code here
    s = [0]
    modify_helper(root, s)
    return root

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
# A utility function to do inorder 
# traversal of BST  
def inorder(root): 
    if root != None: 
        inorder(root.left) 
        print(root.data,end=" ")  
        inorder(root.right)     
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        root = modify(root)
        inorder(root)
        print()
