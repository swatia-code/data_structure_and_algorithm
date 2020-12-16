'''
PROBLEM STATEMENT
-----------------
Given a special Binary Tree whose leaf nodes are connected to form a circular doubly linked list. Find the height of this special Binary Tree.

Example 1:

Input:
        1
      /   \
     2     3
    /
   4
Output: 3
â€‹Explanation: There are 3 edges and 4
nodes in spiral tree where leaf nodes
4 and 3 are connected in circular
doubly linked list form. Thus the
height of spiral tree is 3.
Example 2:

Input:
        1
      /   \
     2     3
    / \
   4   5
  /
 6
Output: 4
Your Task:
You don't need to read input or print anything. Your task is to complete the function findTreeHeight() which takes the root of the special Binary Tree as its input and returns the Height of this special Binary Tree.
In a special Binary Tree, the leaf nodes form a circular doubly linked list.
For Example:

      1
     /   \ 
    2    3
   /  \
  4  5
 /  
6 

In the above binary tree, 6, 5 and 3 are leaf nodes and they form a circular doubly linked list. Here, the left pointer of leaf node will act as a previous pointer of circular doubly linked list and its right pointer will act as next pointer of circular doubly linked list.

Expected Time Complexity: O(Height of the Tree).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <= Number of nodes <= 104

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
def is_leaf(root):
    if root is None:
        return False
        
    return root.left and root.left.right == root and root.right and root.right.left == root
# Return the height of the given special binary tree
def findTreeHeight(root):
    #code here
    if root is None:
        return 0
        
    if is_leaf(root):
        return 1
        
    return 1 + max(findTreeHeight(root.left), findTreeHeight(root.right))


