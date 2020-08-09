'''
PROBLEM STATEMET
----------------
Given a Binary Tree. Check whether it is Symmetric or not, i.e. whether the binary tree is a Mirror image of itself or not.

Input:
First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denote node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output:
For each test case the function should return a boolean value.

Your Task:
You don't need to read input or print anything. Your task is to complete the function isMirror() which takes the root of the Binary Tree as its input and returns True if the given Binary Tree is a same as the Mirror image of itself. Else, it returns False.

For example:
The following binary tree is symmetric:

        1
      /   \
    2       2
  /   \   /   \
 3     4 4     3
But the following is not:

       1
     /   \
    2      2
     \      \
      3      3
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
3
5 1 1 2 N N 2
5 10 20 20 20 N 30
100 10 10 20 20 20 20
Output:
True
False
True
Explanation:
TestCase 1:

             5
           /   \
          1     1
         /       \
        2         2
Tree is mirror image of itself i.e. tree is symmetric

TestCase 2:

             5
          /    \
        10      20
      /    \      \
    20     20      30 
Tree is not mirror image of itself i.e. tree is not symmetric

TestCase 3:

              100
            /     \
          10       10
         /   \    /   \
       20     20 20    20
Tree is mirror image of itself i.e. tree is symmetric


LOGIC
-----
Note that for a symmetric that elements at every level are palindromic. In example 2, at the leaf level- the elements are which is not palindromic.
In other words,
1. The left child of left subtree = right child of right subtree.
2. The right child of left subtree = left child of right subtree.
If we insert the left child of left subtree first followed by right child of the right subtree in the queue, we only need to ensure that these are equal.
Similarly, If we insert the right child of left subtree followed by left child of the right subtree in the queue, we again need to ensure that these are equal.

SOURCE
------
geeksforgeeks

CODE
----
'''
def isSymmetric(root):
    if root is None:
        return True
        
    if root.right is None and root.left is None:
        return True
        
    q = list()
    
    q.append(root)
    q.append(root)
    
    left_node = None
    right_node = None
    
    while len(q):
        
        left_node = q[0]
        q.pop(0)
        
        right_node = q[0]
        q.pop(0)
        
        if left_node.data != right_node.data:
            return False
            
        if left_node.left and right_node.right:
            q.append(left_node.left)
            q.append(right_node.right)
        elif left_node.left or right_node.right:
            return False
            
        if left_node.right and right_node.left:
            q.append(left_node.right)
            q.append(right_node.left)
        elif left_node.right or right_node.left:
            return False

    return True

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
        if isSymmetric(root):
            print("True")
        else:
            print("False")
