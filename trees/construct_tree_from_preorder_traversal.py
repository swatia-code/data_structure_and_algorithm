'''
PROBLEM STATEMENT
-----------------
Given an array pre[] that represents Preorder traversal of a binary tree. One more array preLN[] is given which has only two possible values ‘L’ and ‘N’. The value ‘L’ in preLN[] indicates that the corresponding node in Binary Tree is a leaf node and value ‘N’ indicates that the corresponding node is the non-leaf node.

Note: it is a special binary tree where every node has either 0 or 2 children​

Input:
There will be T, test cases and for each test case, the function will be called separately.
The function takes three arguments as input, first, an integer N, denoting the size of both the array, second an array pre[] that represents Preorder traversal of the binary tree and the last argument a character array preLN[] which indicates that the corresponding node in Binary Tree is a leaf node or a normal node.

Output:
The output will be the inorder traversal of the resultant tree.

User Task:
Your task is to complete the function constructTree(), that constructs the tree from the given two arrays and return the root pointer to new binary tree formed.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <=T <= 100
1 <= N <= 100
1 <= pre[i] <= 100
preLN[i]: {'N', 'L'}

Example:
Input:
3
5
10 30 20 5 15 
N N L L L 
4
1 2 4 3 
N N L L 
6
1 2 4 6 5 3 
N N N L L L

Output:
20 30 5 10 15 
4 2 3 1 
6 4 5 2 3 1 

Explanation:
Testcase 1: Binary tree for the given pre array is:

The inorder traversal of given binary tree is: 20 30 5 10 15.

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
def constructTree(pre, preLN, n):
    '''
    Param: pre:  list of Preorder traversal of tree
    param:  preln: list indicating leaf or node
    param: n: no of nodes
    '''
    # code here
    
    if not pre:
        return
    
    root = Node(pre[0])
    t_list = [root]
    
    for i in range(1, n):
        curr_node = Node(pre[i])
        
        parent_position_type = len(t_list) - 1
        if preLN[parent_position_type] == "N":
            t_list[-1].left = curr_node
        
        else:
            reverse_t = t_list[::-1]
            len_rev = len(reverse_t)
            for i in range(len_rev):
                if preLN[len_rev - i -1] == "N":
                    if not reverse_t[i].left:
                        reverse_t[i].left = curr_node
                        break
                    elif not reverse_t[i].right:
                        reverse_t[i].right = curr_node
                        break
        t_list.append(curr_node)
    
    return root
    
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.data,end=' ')
    printInorder(root.right)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        pre = list(map(int, input().strip().split()))  # nodes
        preln=list(map(str, input().strip().split()))   # leaf or not
        # construct the tree according to given list
        root=constructTree(pre, preln, n)
        printInorder(root)
        print()

