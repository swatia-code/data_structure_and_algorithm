'''
PROBLEM STATEMENT
-----------------
Given a binary tree in which each node element contains a number. Find the maximum possible sum from one leaf node to another.

Input Format:
The first line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denote node values, and a character “N” denotes NULL child.

For example:



For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N
There are multiple test cases. For each test case, the function will be called individually.

Output Format:
For each testcase, in a new line, print the maximum possible sum between two leaf nodes.

Your Task:
Complete the function maxPathSum() that returns the maximum sum from one leaf to another.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(H).
Note: H is the height of the tree and this space is used implicitly for recursion stack.

Constraints:
1 <=T <= 100
3 <= N <= 104
-1000 <= Data on Node <= 1000

Example:
Input:
2
3 4 5 -10 4
-15 5 6 -8 1 3 9 2 -3 N N N N N 0 N N N N 4 -1 N N 10 N

Output:
16
27

Explanation:
Testcase 2: The maximum possible sum from one leaf node to another is (3 + 6 + 9 + 0 + -1 + 10 = 27)


LOGIC
-----
We can find the maximum sum using single traversal of binary tree. The idea is to maintain two values in recursive calls
1) Maximum root to leaf path sum for the subtree rooted under current node.
2) The maximum path sum between leaves (desired output).

For every visited node X, we find the maximum root to leaf sum in left and right subtrees of X. We add the two values with X->data, and compare the sum with maximum path sum found so far.

SOURCE
------
GEEKSFORGEEKS

CODE
----
'''
def max_path_util(root, res):
    
    if root is None:
        return 0
        
    if root.left is None and root.right is None:
        return root.data
        
    left_sum = max_path_util(root.left, res)
    right_sum = max_path_util(root.right, res)
    
    if root.left and root.right:
        res[0] = max(res[0], left_sum + right_sum + root.data)
        return max(left_sum, right_sum) + root.data
        
    if root.left:
        return root.data + left_sum
    else:
        return root.data + right_sum
    
def maxPathSum(root):
    # code here 
    res = [float('-inf')]
    max_path_util(root, res)
    
    return res[0]

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
        print(maxPathSum(root))
