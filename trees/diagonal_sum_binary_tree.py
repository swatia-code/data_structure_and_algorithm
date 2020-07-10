'''
PROBLEM STATEMENT
-----------------
Consider Red lines of slope -1 passing between nodes (in following diagram). The diagonal sum in a binary tree is the sum of all node’s data lying between these lines. Given a Binary Tree of size N, print all diagonal sums.

For the following input tree, output should be 9, 19, 42.
9 is sum of 1, 3 and 5.
19 is sum of 2, 6, 4 and 7.
42 is sum of 9, 10, 11 and 12.

DiagonalSum

Input:
First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output:
Print space separated integers which are the diagonal sums for every diagonal present in the tree with slope -1.

Your Task:
You don't need to take input. Just complete the function diagonalSum() that takes root node of the tree as parameter and returns an array containing the diagonal sums for every diagonal present in the tree with slope -1.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1<=T<=30
1<=N<=105

Example:
Input:
2
4 1 3 N N 3
10 8 2 3 5 2
Output:
7 4 
12 15 3 


LOGIC
-----
The idea is to keep track of vertical distance from top diagonal passing through root. We increment the vertical distance we go down to next diagonal.
1. Add root with vertical distance as 0 to the queue.
2. Process the sum of all right child and right of right child and so on.
3. Add left child current node into the queue for later processing. The vertical distance of left child is vertical distance of current node plus 1.
4. Keep doing 2nd, 3rd and 4th step till the queue is empty.

SOURCE
------
geeksforgeeks

CODE
----
'''
def diagonal_sum_helper(root, d, diagonal):
    if root is None:
        return None
        
    if d not in diagonal:
        diagonal[d] = root.data
    else:
        diagonal[d] += root.data

    diagonal_sum_helper(root.left, d + 1, diagonal)
    diagonal_sum_helper(root.right, d, diagonal)
    
def diagonalSum(root):
    #:param root: root of the given tree.
    
    #code here
    diagonal = dict()
    
    diagonal_sum_helper(root, 0, diagonal)
    
    res = list()
    for d in sorted(diagonal):
        res.append(diagonal[d])
        
    return res


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
        res = diagonalSum(root)
        for i in res:
            print (i, end = " ")
        print()
