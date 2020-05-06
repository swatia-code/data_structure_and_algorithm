"""
PROBLEM STATEMENT
-----------------
Given a Binary Tree, convert it into its mirror.
MirrorTree1            

Input:
First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:


For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output:
For each testcase, in a new line, print inorder traversal of mirror tree.

Your Task:
You don't have to take any input. Just complete the function mirror() that takes node as paramter. The printing is done by the driver code.

Constraints:
1 <= T <= 100
1 <= Number of nodes <= 100
1 <= Data of a node <= 1000

Example:
Input:
2
1 3 2
10 20 30 40 60
Output:
2 1 3
30 10 60 20 40

Explanation:
Testcase1: The tree is
        1         (mirror)     1
     /      \         =>        /     \
   3       2                  2         3
The inorder of mirror is 2 1 3
Testcase2: The tree is
                           10                                      10
                        /        \           (mirror)         /        \
                     20         30            =>        30        20
                  /       \                                              /    \
               40       60                                        60    40
The inroder traversal of mirror is 30 10 60 20 40.

LOGIC
-----
1. Recursive approach:
a) Swap left and right subtree
	temp = left subtree
	left subtree = right subtree
	right subtree = temp

b) call function for left subtree
c) call function for right subtree

2. Iterative aproach:
The idea is to do queue based level order traversal. While doing traversal, swap left and right children of every node. Basically it is doing BFS traversal only and while doing BFS, we need to swap left and right children.

SOURCE
------
geeksforgeeks

CODE
----
"""
# your task is to complete this function
# recursive approach
def mirror(root):
    # Code here
    if root == None:
        return 
    
    temp = root.left
    root.left = root.right
    root.right = temp
    
    mirror(root.left)
    mirror(root.right)

def mirror_iterative(root):
    # Code here
    if root == None:
        return 
    
    q = []
    q.append(root)
    
    while len(q):
        
        current = q[0]
        q.pop(0)
        
        current.left, current.right = current.right, current.left
        
        if current.left:
            q.append(current.left)
            
        if current.right:
            q.append(current.right)


#{ 
#  Driver Code Starts
#Initial Template for Python 

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def inorderTraversalUtil(root):
    # Code here
    if root is None:
        return
    inorderTraversalUtil(root.left)
    print(root.data, end=' ')    
    inorderTraversalUtil(root.right)

def inorderTraversal(root):
    # Code here
    inorderTraversalUtil(root)
    print()
    
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
        mirror(root)
        inorderTraversal(root)
        
        

# } Driver Code Ends


