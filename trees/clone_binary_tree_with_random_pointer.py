'''
PROBLEM STATEMENT
------------------
Given a special binary tree having random pointers along with the usual left and right pointers. Clone the given tree.

Example 1:

Input:

Output: 1
Explanation: The tree was cloned successfully.

Your Task:
No need to read input or print anything. Complete the function cloneTree() which takes root of the given tree as input parameter and returns the root of the cloned tree. 

Note: The output is 1 if the tree is cloned successfully. Otherwise output is 0.


Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).


Constraints:
1 <=Number of nodes<= 100
1 <=Data of a node<= 1000

LOGIC
-----
The idea is to store mapping from given tree nodes to clone tree nodes in hashtable. Following are detailed steps.

1) Recursively traverse the given Binary and copy key value, left pointer and right pointer to clone tree. While copying, store the mapping from given tree node to clone tree node in a hashtable. In the following pseudo code, ‘cloneNode’ is currently visited node of clone tree and ‘treeNode’ is currently visited node of given tree.

   cloneNode->key  = treeNode->key
   cloneNode->left = treeNode->left
   cloneNode->right = treeNode->right
   map[treeNode] = cloneNode 
2) Recursively traverse both trees and set random pointers using entries from hash table.

SOURCE
------
geeksforgeeks

CODE
----
'''
def clone_left_right(node, freq):
    if node is None:
        return None
        
    clone_node = Node(node.data)
    freq[node] = clone_node
    clone_node.left = clone_left_right(node.left, freq)
    clone_node.right = clone_left_right(node.right, freq)
    
    return clone_node
    
def clone_random_pointer(tree_node, clone_node, freq):
    if tree_node is not None:
        if freq.get(tree_node.random):
            clone_node.random = freq[tree_node.random]
        clone_random_pointer(tree_node.left, clone_node.left, freq)
        clone_random_pointer(tree_node.right, clone_node.right, freq)

def cloneTree(node):
    #code here
    freq = dict()
    root = clone_left_right(node, freq)
    clone_random_pointer(node, root, freq)
    
    return root


#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.random=None

    def __str__(self):
        return str(self.data)

def printInord(a,b):
    if (not a and not b) or (not a.random and not b.random):
        return 1
    if a.random.data==b.random.data and printInord(a.left,b.left) and printInord(a.right,b.right):
        return 1
    return False


if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        map=dict()

        n=int(input())
        arrnode=[x for x in input().split()]

        root=None
        i=0
        while i<3*n:

            n1,n2,lr=int(arrnode[i]),int(arrnode[i+1]),arrnode[i+2]

            if n1 in map:
                parent=map[n1]
            else:
                parent = Node(n1)
                map[n1] = parent

                if not root:
                    root = parent


            child=Node(n2)
            map[n2]=child

            if lr=='R':
                parent.right=child

            elif lr=='L':
                parent.left=child

            else:
                parent.random=map[n2]


            i+=3

        ansTree=cloneTree(root)

        if ansTree==root:
            print(0)
        else:
            print(printInord(root,ansTree))





# } Driver Code Ends
