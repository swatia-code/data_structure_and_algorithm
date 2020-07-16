'''
PROBLEM STATEMENT
-----------------
Given a sorted array. Write a program that creates a Balanced Binary Search Tree using array elements. If there are N elements in array, then floor(n/2)'th element should be chosen as root and same should be followed recursively.

Input:
The first line of input contains an integer T, denoting the number of test cases. The first line of each test case is N(size of array). The second line of each test case contains N input A[].

Output:
Print the preorder traversal of constructed BST.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 1000
1 ≤ A[i] ≤ 10000

Example:
Input:
1
7
1 2 3 4 5 6 7

Output:
4 2 1 3 6 5 7

LOGIC
-----
1) Get the Middle of the array and make it root.
2) Recursively do same for left half and right half.
      a) Get the middle of left half and make it left child of the root
          created in step 1.
      b) Get the middle of right half and make it right child of the
          root created in step 1.

SOURCE
------
geeksforgeeks

CODE
----
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
def array_to_bst(l):
    if len(l) == 0:
        return None
        
    n = len(l)
    
    if n % 2 == 0:
        mid = int((n / 2) - 1)
    else:
        mid = n // 2
    
    root = Node(l[mid])
    
    root.left = array_to_bst(l[:mid])
    root.right = array_to_bst(l[mid + 1:])
    
    return root

def preorder(root):
    if root is None:
        return
    
    print(root.data,end = " ")
    preorder(root.left)
    preorder(root.right)
    

t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    root = array_to_bst(l)
    preorder(root)
    print()
