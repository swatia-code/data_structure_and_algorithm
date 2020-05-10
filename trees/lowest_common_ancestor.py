"""
PROBLEM STATEMENT
-----------------
Given a Binary Tree with all unique values and two nodes value n1 and n2. The task is to find the lowest common ancestor of the given two nodes. We may assume that either both n1 and n2 are present in the tree or none of them is present. 

Input:
The first line of input contains the number of test cases T. For every test case, the first line of input contains two space-separated integers, denoting node values for which we want to find LCA,  and the second line will contain a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denote node values, and a character “N” denotes NULL child.

For example:

 
For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output:
For each test case, in a new line, print the Lowest Common Ancestor of the two nodes.

Your Task:
This is a function problem. You don't have to read the input. Just complete the function lca() that takes nodes, n1, and n2 as parameters and returns LCA node as output.

Constraints:
1 <= T <= 100
1 <= Number of nodes <= 100
1 <= Data of a node <= 1000

Example:
Input:
2
2 3
1 2 3
3 4
5 2 N 3 4
Output:
1
2

Explanation:
Testcase1: The tree is
        1
     /      \
   2        3
The LCA of 2 and 3 is 1.
Testcase 2: The tree is
          5
        /
      2
     /   \
   3     4
The lowest common ancestor of given node 3 and 4 is 2.

LOGIC
-----
If any of the given keys(n1 and n2) matches with root, then root is LCA. If root doesn't match with any of the keys, we recur for the left and right subtree. The node which has one key present in it's left subtree and the other key present in right subtree is the LCA. If both keys lie in left subtree, then left subtree has LCA also, otherwise LCA lies in right subtree.

SOURCE
------
geeksforgeeks

CODE
----
"""



def find(root, n):
    if root == None:
        return False
    
    if root.data == n:
        return True
        
    if find(root.left, n) or find(root.right, n):
        return True
        
    return False

def lca_helper(root, n1, n2, v):
    
    if root == None:
        return None
        
    if root.data == n1:
        v[0] = True
        return root
        
    if root.data == n2:
        v[1] = True
        return root
        
    left_lca = lca_helper(root.left, n1, n2, v)
    right_lca = lca_helper(root.right, n1, n2, v)
    
    if left_lca and right_lca :
        return root
        
    return left_lca if left_lca else right_lca

def lca(root, n1, n2):
    # Code here
    v = [False, False]
    
    res = lca_helper(root, n1, n2, v)

    if (v[0] and v[1] or find(root, n1) and v[1] or find(root, n2) and v[0]):
        return res
        
    return None



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
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        a,b=list(map(int,input().split()))
        s=input()
        root=buildTree(s)
        k=lca(root,a,b)
        print(k.data)



# } Driver Code Ends
