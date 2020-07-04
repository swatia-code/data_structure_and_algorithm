'''
PROBLEM STATEMENT
-----------------
Complete the function to print spiral order traversal of a tree. For below tree, function should print 1, 2, 3, 4, 5, 6, 7.


 
 

Input:
First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output:
The function should print level order traversal in spiral form.

Your Task:
The task is to complete the function printSpiral() which prints the elements in spiral form of level order traversal. The newline is automatically appended by the driver code.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= T <= 30
0 <= Number of nodes <= 105
1 <= Data of a node <= 105

Example:
Input:
2
1 3 2  
10 20 30 40 60 
Output:
1 3 2
10 20 30 60 40 

Explanation:
Testcase1: The tree is
        1
     /      \
   3       2
So, the spiral level order would be 1 3 2
Testcase2: The tree is
                           10
                        /        \
                     20         30
                  /       \
               40       60
So, the spiral level order would be 10 20 30 60 40
 

LOGIC
-----
same as zigzag_tree_traversal.py

SOURCE
------
geeksforgeeks

CODE
----
'''
def printSpiral(root):
    # Code here
    if (root == None): 
        return None

    s1 = [] 
    s2 = [] 
    s1.append(root) 
	
    while not len(s1) == 0 or not len(s2) == 0: 
        while not len(s1) == 0: 
            temp = s1[-1] 
            s1.pop() 
            print(temp.data, end = " ") 
            if (temp.right): 
                s2.append(temp.right) 
            if (temp.left): 
                s2.append(temp.left) 

        while (not len(s2) == 0): 
            temp = s2[-1] 
            s2.pop() 
            print(temp.data, end = " ") 
            if (temp.left): 
                s1.append(temp.left) 
            if (temp.right): 
                s1.append(temp.right) 

from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def buildTree(s):
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
        currNode=q[0]
        q.popleft()
        size=size-1
        
        currVal=ip[i]
        
        if(currVal!="N"):
            
            currNode.left=Node(int(currVal))
            
            q.append(currNode.left)
            size=size+1
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        if(currVal!="N"):
            
            currNode.right=Node(int(currVal))
            
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        printSpiral(root)
        print()
