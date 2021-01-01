"""
PROBLEM STATEMENT
-----------------
Given a Binary Tree, write a function to check whether the given Binary Tree is a prefect Binary Tree or not. A Binary tree is Perfect Binary Tree in which all internal nodes have two children and all leaves are at same level.

Input:
First line of input contains the number of test cases T. For each test case, there will be two lines: 

First line of each test case will be an integer N denoting the number of parent child relationships.

Second line of each test case will print the level order traversal of the tree in the form of N space separated triplets. The description of triplets is as follows:

Each triplet will contain three space-separated elements of the form (int, int char).

The first integer element will be the value of parent. 

The second integer will be the value of corresponding left or right child. In case the child is null, this value will be -1.

The third element of triplet which is a character can take any of the three values ‘L’, ‘R’ or ‘N’. L denotes that the children is a left child, R denotes that the children is a Right Child and N denotes that the child is NULL.

Please note that the relationships are printed only for internal nodes and not for leaf nodes.

Output:
Print "Yes" (without quotes) if the binary tree is perfect binary tree.
Print "No" (without quotes) if the binary tree is not a perfect binary tree.
Driver code will print the output based upon the value returned by function.

Your Task:
Finish the function such that it returns 1 if the given tree is perfect binary tree and 0 if not.

Constraints:
1<=T<=10^5
1<=N<=10^5
1<=data of node<=10^5

Example:
Input:
3
6
10 20 L 10 30 R 20 40 L 20 50 R 30 60 L 30 70 R
2
18 15 L 18 30 R
6
1 2 L 1 3 R 2 -1 N 2 4 R 3 5 L 3 6 R

Output: 
Yes
Yes
No

LOGIC
------
Find depth of any node (in below tree we find depth of leftmost node). Let this depth be d.
Now recursively traverse the tree and check for following two conditions.
Every internal node should have both children non-empty
All leaves are at depth ‘d’

SOURCE
------
geeksforgeeks

CODE
----
"""
def isPerfectRec(root, d,level ):
    #code here
    if root is None:
        return True
        
    if root.left is None and root.right is None:
        return d == level + 1
        
    if root.left is None or root.right is None:
        return False
        
    return isPerfectRec(root.left, d, level + 1) and isPerfectRec(root.right, d, level + 1)
    

from collections import deque

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
def findADepth(node):
    d=0
    while(node!=None):
        d=d+1
        node=node.left
    return d
    
def isPerfect(root):
    d=findADepth(root)
    return isPerfectRec(root,d,0)
    
    
    
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
        head=make_tree()
        if(isPerfect(head)):
            print("Yes")
        else:
            print("No")

