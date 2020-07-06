'''
PROBLEM STATEMENT
-----------------
Given a Binary Tree, print the vertical traversal of it starting from the leftmost level to the rightmost level.
If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal of the tree.

Input Format:
First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:
 
For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output Format:
For each testcase, the vertical order traversal of the tree is to be printed. The nodes' data are to be separated by spaces.

Your Task:
You don't need to read input or print anything. Your task is to complete the function verticalOrder() which takes the root node as input and returns an array containing the vertical order traversal of the tree from the leftmost to the rightmost level. If 2 nodes lie in the same vertical level, they should be printed in the order they appear in the level order traversal of the tree.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= T <= 100
1 <= Number of nodes <= 5000

Example:
Input:
3
2 N 3 4 N
1 2 3 4 5 N 6
3 1 5 N 2 4 7 N N N N 6 
Output:
2 4 3
4 2 1 5 3 6
1 3 2 4 5 6 7
Explanation:
Testcase1:
         2
           \
            3
            /
         4
As it is evident from the above diagram that during vertical traversal 2, 4 will come first, then 3. So output is 2 1 5 3
Testcase2:
             1
           /     \
         2       3
      /     \        \
    4       5       6
As it is evident from the above diagram that during vertical traversal 4 will come first, then 2, then 1,5, then 3 and then 6. So the output is 4 2 1 5 3 6.


LOGIC
-----
We can do preorder traversal of the given Binary Tree. While traversing the tree, we can recursively calculate HDs. We initially pass the horizontal distance as 0 for root. For left subtree, we pass the Horizontal Distance as Horizontal distance of root minus 1. For right subtree, we pass the Horizontal Distance as Horizontal Distance of root plus 1. For every HD value, we maintain a list of nodes in a hash map. Whenever we see a node in traversal, we go to the hash map entry and add the node to the hash map using HD as a key in a map.

SOURCE
------
geeksforgeeks

CODE
----
'''


def helper(root, d, hd):
    if not root:
        return
    if hd in d:
        d[hd].append(root.data)
    else:
        d[hd] = [root.data]
    if root.left:
        helper(root.left, d, hd-1)
    if root.right:
        helper(root.right, d, hd+1)

def verticalOrder(root):
#Your code here
    d = dict()
    helper(root,d, 0)
    ans = []
    for k in sorted(d):
        [ans.append(j) for j in d[k]]
    return ans

from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
    
    ip=list(map(str,s.split()))
    
 
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    q.append(root)                            
    size=size+1 
    

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
        res = verticalOrder(root)
        for i in res:
            print (i, end=" ")
        print()
