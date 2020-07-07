'''
PROBLEM STATEMENT
-----------------
Given a binary tree, a target node in the binary tree, and an integer value k, find all the nodes that are at distance k from the given target node. No parent pointers are available.

Input:
First line of input contains the number of test cases T. For each test case, there will be three lines of input first of which is a string representing the tree as described below: 

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N
Second line of test case holds the integer value target.
Third line hold the value k.

Output:
All the space separated nodes that are at distance k from the given target node in sorted order.

Your task:
Your task is to complete the function KDistanceNodes(). This function returns the sorted list of nodes at k distance from target. Returned list will be printed by driver code.

Constraints:
1 <= T <= 200
1 <= no of edges <= 1000
1<= data of node <= 10000
1 <= target <= 10000
1 <= k <= 20

Expected time complexity: O(N)

Expected auxiliary space: O(h) , where h = height of tree

Example:
Input:
2
20 8 22 4 12 N N N N 10 14
8
2
20 7 24 4 3 N N N N 1
7
2

Output:
10 14 22 
1 24

Explanation:
Testcase 1:


we can observe that target node is 8,  and nodes which are at k distant from this target node are 10, 14 and 22.


LOGIC
-----
There are two types of nodes to be considered.
1) Nodes in the subtree rooted with target node.
2) Other nodes, may be an ancestor of target, or a node in some other subtree.

Finding the first type of nodes is easy to implement. Just traverse subtrees rooted with the target node and decrement k in recursive call. When the k becomes 0, print the node currently being traversed 
How to find nodes of second type? For the output nodes not lying in the subtree with the target node as the root, we must go through all ancestors. For every ancestor, we find its distance from target node, let the distance be d, now we go to other subtree (if target was found in left subtree, then we go to right subtree and vice versa) of the ancestor and find all nodes at k-d distance from the ancestor.

SOURCE
------
geeksforgeeks

CODE
----
'''
def subtree_nodes(root, k, l):
    if root == None:
        return
        
    if k == 0:
        l.append(root.data)
        return 
        
    subtree_nodes(root.left, k - 1, l)
    subtree_nodes(root.right, k - 1, l)
    
def k_distance_nodes(root, target, k, l):
      
    if root == None:
        return -1
           
    dl = k_distance_nodes(root.left, target, k, l)
    if dl != -1:
        if dl + 1 == k:
            l.append(root.data)
        else:
            subtree_nodes(root.right, k - dl -2, l)
        return dl + 1
            
    dr = k_distance_nodes(root.right, target, k, l)
    if dr != -1:
        if dr + 1 == k:
            l.append(root.data)
        else:
            subtree_nodes(root.left, k - dr - 2, l)
        return 1 + dr
        
    if root.data == target:
        subtree_nodes(root, k, l)
        return 0 
    
    return -1

class solver:
    
    def KDistanceNodes(self,root,target,k):
        
        l = list()
        k_distance_nodes(root, target, k, l)
        l.sort()
        return l


from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def buildTree(s):
  
    if (len(s) == 0 or s[0] == "N"):
        return None

    ip = list(map(str, s.split()))

    root = Node(int(ip[0]))
    size = 0
    q = deque()

    q.append(root)
    size = size + 1

    i = 1
    while (size > 0 and i < len(ip)):
        currNode = q[0]
        q.popleft()
        size = size - 1

        currVal = ip[i]

        if (currVal != "N"):

            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

if __name__ == "__main__":
    x = solver()
    t = int(input())
    for _ in range(t):
        line = input()
        target=int(input())
        k=int(input())

        root = buildTree(line)
        res = x.KDistanceNodes(root,target,k)
        
        for i in res:
            print(i, end=' ')
        print()
