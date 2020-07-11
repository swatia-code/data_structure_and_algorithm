'''
PROBLEM STATEMENT
-----------------
Given a binary tree and two node values your task is to find the minimum distance between them.

Input:
First line of input contains the number of test cases T. For each test case, there will be only a two lines of input first of which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N
The next line contains two integers denoting two nodes a and b.
There are multiple test cases. For each test case, this method will be called individually.

Output:
The function should return min distance between two node values.

Your Task:
You don't need to read input or print anything. Your task is to complete the function findDist() which takes the root node of the Tree and the two node values as inputs and returns the minimum distance between the nodes represented by the two given node values.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <= T <= 100
1 <= Number of nodes <= 104
1 <= Data of a node <= 105

Example:
Input
1
2
1 2 3
2 3 

Output
2

Explanation:
Test Case 1: The tree formed is:
      1
     /   \ 
   2     3
We need the distance between 2 and 3. Being at node 2, we need to take two steps ahead in order to reach node 3. The path followed will be: 2 -> 1 -> 3. Hence, the result is 2. 

LOGIC
-----
We first find LCA of two nodes. Then we find distance from LCA to two nodes.

SOURCE
-----
geeksforgeeks

CODE
----
'''
def lca_helper(root, a, b):
    if root is None:
        return None
        
    if root.data == a or root.data == b:
        return root
        
    left_lca = lca_helper(root.left, a, b)
    right_lca = lca_helper(root.right, a, b)
    
    if left_lca and right_lca:
        return root
        
    if left_lca:
        return left_lca
    else:
        return right_lca
        
def find_distance(root, val, d, dis):
    if root is None:
        return 
    
    if root.data == val:
        d.append(dis)
        return 
    
    find_distance(root.left, val, d, dis + 1)
    find_distance(root.right, val, d, dis + 1)

def findDist(root,a,b):
    
    lca = lca_helper(root, a, b)
    d1 = list()
    d2 = list()
    
    if lca:
        find_distance(lca, a, d1, 0)
        find_distance(lca, b, d2, 0)
        return d1[0] + d2[0]
    else:
        return -1


import sys
sys.setrecursionlimit(50000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


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
        a, b=map(int, input().split())
        print(findDist(root, a, b))

