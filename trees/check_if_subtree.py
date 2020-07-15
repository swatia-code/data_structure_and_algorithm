'''
PROBLEM STATEMENT
-----------------
Given two binary trees with head reference as T and S having at most N nodes. The task is to check if S is present as subtree in T.
A subtree of a tree T1 is a tree T2 consisting of a node in T1 and all of its descendants in T1.

Example:

S:          10
              /   \
            4     6
                 /
             30

T:                  26
                      /   \
                    10   3
                   /   \     \

               4       6     3
                       /
                    30

In above example S is subtree of T.

Please note that subtree has to be having same leaves non leaves.

   10
  /
20

For example, above tree is not subtree of

         10
       /     \
    20     50
   /   \
30   40

But a subtree of

         30
       /     \
    10     50
   /  
20  

Input:
First line of input contains the number of test cases T. For each test case, there will be two lines of input each of which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N.

First string denotes tree T and second string denotes tree S.

Output:
For each testcase, there will be a single line containing 0 or 1, depending on the input.

Your Task:
Complete the function isSubtree() that takes two nodes as parameter and returns true or false.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= T <= 100
1 <= N <= 104

Example:
Input:
3
1 2 3 N N 4
3 4
26 10 N 20 30 40 60
26 10 N 20 30 40 60
26 10 3 4 6 N 3 N N N 25
10 4 6 N 30
Output:
1
1
0

Explanation:
Testcase 1: Given trees are 
T:                   1                                                        S:                   3
                   /      \                                                                          /
                 2       3                                                                       4
               /    \    /   
             N    N  4
S is the subtree in T.
Testcase 2: Given trees are
T:                    26                                                         S:                              26
                    /        \                                                                                     /       \
                  10       N                                                                                 10       N
                 /      \                                                                                      /       \
               20    30                                                                                  20      30
             /      \                                                                                      /       \
          40     60                                                                                  40      60
S is present as subtree in T.
Testcase 3: Given trees are
T:                                   26                                                      S:                                      10
                                     /    \                                                                                               /   \
                                   10    3                                                                                           4    6
                                    / \      \                                                                                            \
                                   4  6     3                                                                                          30
                                         \
                                          25
10 is root node of tree. Left child of 10 is 4 and right child of 10 is 6. Right child of 4 is 30.

 
LOGIC
-----
Traverse the tree T in preorder fashion. For every visited node in the traversal, see if the subtree rooted with this node is identical to S.

SOURCE
------
geeksforgeeks

CODE
----
'''
def are_identical(T1, T2):
    if T1 is None and T2 is None:
        return True
        
    if T1 is None or T2 is None:
        return False
        
    return (T1.data == T2.data) and are_identical(T1.left, T2.left) and are_identical(T1.right, T2.right)


def isSubTree(T1, T2):
    # Code here
    if T2 is None:
        return True
        
    if T1 is None:
        return False
        
    if are_identical(T1, T2):
        return True
        
    return isSubTree(T1.left, T2) or isSubTree(T1.right, T2)

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
        rootT=buildTree(input())
        rootS=buildTree(input())
        if isSubTree(rootT, rootS) is True:
            print("1")
        else:
            print("0")
