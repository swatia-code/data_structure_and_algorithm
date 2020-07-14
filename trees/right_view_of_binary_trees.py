'''
PROBLEM STATEMENT
-----------------
Given a Binary Tree, print Right view of it. Right view of a Binary Tree is set of nodes visible when tree is viewed from right side.

Right view of following tree is 1 3 7 8.

          1
       /     \
     2        3
   /   \      /    \
  4     5   6    7
    \
     8

Input :
First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output :
For each test case, in a new line, print the right view of the binary tree.

Your Task:
This is a function problem. You don't have to take input. Just complete the function rightView() that takes node as parameter and prints the right view. The newline is automatically appended by the driver code.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <= T <= 100
1 <= Number of nodes <= 105
1 <= Data of a node <= 105

Example:
Input:
2
1 3 2
10 20 30 40 60
Output:
1 2
10 30 60

Explanation:
Test case 1: Below is the given tree

           1
         /     \
      3        2
For the above test case the right view is: 1 2
Test case 2: Below is the given tree

            10
         /        \
     20          30
   /      \      
40      60

Right View is: 10 30 60.

LOGIC
-----
The Right view contains all nodes that are last nodes in their levels. A simple solution is to do level order traversal and print the last node in every level.

The problem can also be solved using simple recursive traversal. We can keep track of level of a node by passing a parameter to all recursive calls. The idea is to keep track of maximum level also. And traverse the tree in a manner that right subtree is visited before left subtree. Whenever we see a node whose level is more than maximum level so far, we print the node because this is the last node in its level (Note that we traverse the right subtree before left subtree). Following is the implementation of this approach.

SOURCE
------
geeksforgeeks

CODE
----
'''
def right_view_helper(root, level, max_level):
    if root is None:
        return 
    
    if (max_level[0] < level):
        print(root.data, end=" ")
        max_level[0] = level
        
    right_view_helper(root.right, level + 1, max_level)
    right_view_helper(root.left, level + 1, max_level)

def rightView(root):
    '''
    :param root: root of given tree.
    :return: print the right view of tree, dont print new line
    '''
    # code here
    max_level = [0]
    right_view_helper(root, 1, max_level)

from collections import deque
import queue
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
        rightView(root)
        print()
