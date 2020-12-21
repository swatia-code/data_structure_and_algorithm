'''
PROBLEM STATEMENT
-----------------
Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

       1
    /     \
   2       3
  /  \    /   \
4    5  6   7

Top view will be: 4 2 1 3 7
Note: Print from leftmost node to rightmost node.

Example 1:

Input:
      1
   /    \
  2      3
Output: 2 1 3

Example 2:

Input:
       10
    /      \
  20        30
 /   \    /    \
40   60  90    100
Output: 40 20 10 30 100
Your Task:
Since this is a function problem. You don't have to take input. Just complete the function printTopView() that takes root node as parameter and prints the top view. The newline is automatically appended by the driver code.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 105
1 <= Node Data <= 105
 
LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def top_view_helper(root, top_view_node, hd, level):
    if root is None:
        return
    
    if hd not in top_view_node:
        top_view_node[hd] = [root.data, level] 
    elif hd in top_view_node and level < top_view_node[hd][1]:
        top_view_node[hd] = [root.data, level]
        
    top_view_helper(root.left, top_view_node, hd - 1, level + 1)
    top_view_helper(root.right, top_view_node, hd + 1, level + 1)

def topView(root):
    '''
    :param root: root of the binary tree
    :return: None, newline is provided by driver code
    '''
    # code here
    top_view_node = dict()
    hd = 0
    level = 0
    top_view_helper(root, top_view_node, hd, level)
    
    for key in sorted(top_view_node):
        print(top_view_node[key][0], end=" ")



#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Contributed by Sudarshan Sharma

from collections import deque
import queue 

class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
def make_tree():
    n=int(input())
    l=list(map(str,input().split()))
    head=None
    q=deque()
    i=0
    while(n>0):
        a,b,c=l[i],l[i+1],l[i+2]
        if(not head):
            head=Node(int(a))
            q.append(head)
        pick=q[0]
        q.popleft()
        if(c=='L'):
            pick.left=Node(int(b))
            q.append(pick.left)
        n=n-1
        if(not n):
            break
        a,b,c=l[i+3],l[i+4],l[i+5]
        if(c=='R'):
            pick.right=Node(int(b))
            q.append(pick.right)
        i=i+6
        n=n-1
    return head
            

if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        root=make_tree()
        topView(root)
        print()

# } Driver Code Ends
