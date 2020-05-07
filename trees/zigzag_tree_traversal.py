"""
PROBLEM STATEMENT
-----------------
Given a binary tree of size N, your task is to complete the function zigZagTraversal(), that prints the nodes of binary tree in ZigZag manner.

First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:


For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output:
For each test case print on a new line space-separated all the nodes of the tree in ZigZag manner.

Constraints:
1 <= T <= 100
1 <= N <= 104

Example:
Input:
2
3 2 1
7 7 9 8 8 6 N 10 9
Output:
3 1 2
7 9 7 8 8 6 9 10

Explanation:
Testcase 1: Given tree is
                         3
                      /       \
                    2        1
Hence the zigzag traversal will be 3 1 2.
Testcase 2: Given tree is 
                           7
                       /        \
                    9           7
                /        \      /     \
               8        8    6     N
            /      \
          10     9  
Hence the zigzag traversal will be 7 9 7 8 8 6 9 10.


LOGIC
-----
This problem can be solved using two stacks. Assume the two stacks: currentlevel and nextlevel. We would also need a variable to keep track of the current levelorder(whether it is left to right or right to left). We pop from the currentlevel stack and print the node value and swap the two stacks at the end of each level and change flag value.

SOURCE
------
geeksforgeeks

CODE
----
"""

def zigZagTraversal(root):
    '''
    param: root:   root of tree
    return None, no need to print new line
    '''
    if root == None:
        return
    
    curr_level = []
    next_level = []
    
    curr_level.append(root)
    flag = True
    
    while len(curr_level)>0:
        curr = curr_level.pop(-1)
        print(curr.data,end = ' ')
        
        if flag:
            if curr.left:
                next_level.append(curr.left)
            if curr.right:
                next_level.append(curr.right)
                
        else:
            if curr.right:
                next_level.append(curr.right)
            if curr.left:
                next_level.append(curr.left)
                
                
        if len(curr_level)==0:
            flag = not flag
            curr_level,next_level = next_level,curr_level
        
    
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3
from collections import defaultdict
from collections import deque

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
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
    
if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        zigZagTraversal(root)
        print()
# } Driver Code Ends
