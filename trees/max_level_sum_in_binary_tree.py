"""
PROBLEM STATEMENT
-----------------
Given a Binary Tree having positive and negative nodes. Find the maximum sum of a level in the given Binary Tree.

Example 1:

Input :               
             4
          /    \
         2     -5
        / \    / \
      -1   3  -2  6

Output: 6

Explanation :
Sum of all nodes of 0'th level is 4
Sum of all nodes of 1'th level is -3
Sum of all nodes of 2'th level is 6
Hence maximum sum is 6

Example 2:

Input :          
            1
          /   \
         2     3
        / \     \
       4   5     8
                / \
               6   7  

Output :  17

Explanation: Maximum sum is at level 2.

Your Task:  
You dont need to read input or print anything. Complete the function maxLevelSum() which takes root node as input parameter and returns the maximum sum of any horizontal level in the given Binary Tree.


LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
"""
# function should return max sum level in the tree
'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''
def max_level_sum_helper(root, level, level_sum):
    if root is None:
        return
    
    if level not in level_sum:
        level_sum[level] = root.data
    else:
        level_sum[level] += root.data
        
    max_level_sum_helper(root.left, level + 1, level_sum)
    max_level_sum_helper(root.right, level + 1, level_sum)

def maxLevelSum(root):
    # Code here
    level_sum = dict()
    max_level_sum_helper(root, 0, level_sum)
    
    max_val = float('-inf')
    for ele in level_sum:
        max_val = max(max_val, level_sum[ele])
        
    return max_val
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
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
    for _ in range(t):
        s=input()
        root=buildTree(s)
        print(maxLevelSum(root))

# } Driver Code Ends
