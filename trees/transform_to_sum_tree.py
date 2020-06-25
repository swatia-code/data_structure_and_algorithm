'''
PROBLEM STATEMENT
-----------------
Given a Binary Tree of size N , where each node has positive and negative values. Convert this to a tree where each node contains the sum of the left and right sub trees in the original tree. The values of leaf nodes are changed to 0.

For example, the following tree

             10
          /      \
        -2        6
       /   \     /  \
     8     -4   7    5

should be changed to

       20(4-2+12+6)
          /              \
     4(8-4)      12(7+5)
       /   \           /  \
     0      0       0    0

 

Input:
First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N


Output:
Inorder traversal of modified tree , printed by driver code.

Your Task:
You don't need to take input. Just complete the function toSumTree() which accepts root node of the tree as a parameter and modify tree into SumTree.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <=T<= 100
1 <= N <= 104

Example:
Input:
2
3 1 2
10 20 30 40 60

Output:
0 3 0
0 100 0 150 0


LOGIC
-----
Do a traversal of the given tree. In the traversal, store the old value of the current node, recursively call for left and right subtrees and change the value of current node as sum of the values returned by the recursive calls. Finally return the sum of new value and value (which is sum of values in the subtree rooted with this node).

SOURCE
------
geeksforgeeks

CODE
----
'''

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def toSumTree(root) :
    '''
    :param root: root of the given tree.
    '''
    #code here
    if root == None:
        return 0
        
    val = root.data
    
    root.data = toSumTree(root.left) + toSumTree(root.right)
    
    return root.data + val


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
    
# A utility function to print  
# inorder traversal of a Binary Tree  
def printInorder(Node) : 
    if (Node == None) : 
        return
    printInorder(Node.left)  
    print(Node.data, end = " ")  
    printInorder(Node.right)  
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        toSumTree(root)
        printInorder(root)
        print()
# } Driver Code Ends
