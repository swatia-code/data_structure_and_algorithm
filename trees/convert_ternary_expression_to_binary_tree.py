'''
PROBLEM STATEMENT
-----------------
Given a string that contains ternary expressions. The expressions may be nested. You need to convert the given ternary expression to a binary Tree and return the root.

Input Format:
First line of input contains of test case T. The only line of test case consists of String s.

Outpu Format:
Preorder traversal of Tree formed

Your Task:
This is a function problem, you don't need to read input/output. Just complete the function convertExpression that take string and index(initialized from 0) as parameters.

Constraints:
1 <= T <= 100
1 <= |String| <= 100

Example:
Input:
2
a?b:c
a?b?c:d:e
Output:
a b c
a b c d e

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''

def convert_expression(expression, i):
    if i >= len(expression): 
        return None
 
    root = Node(expression[i]) 
  
    i += 1
  
    if (i < len(expression) and 
                expression[i] is "?"): 
        root.left = convert_expression(expression, i + 1) 
          
    elif i < len(expression): 
        root.right = convert_expression(expression, i + 1) 
    return root 


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10000)

class Node: 
    def __init__(self, key): 
        self.data = key 
        self.left = None
        self.right = None
  
# Function to print the tree 
# in a pre-order traversal pattern 
def print_tree(root): 
    if not root: 
        return
    print(root.data, end=' ') 
    print_tree(root.left) 
    print_tree(root.right) 
  
# Driver Code 
if __name__ == "__main__": 

    tcs=int(input())
    for _ in range(tcs):
        expression=input()
        root_node=convert_expression(expression, 0) 
        print_tree(root_node) 
        print()
# } Driver Code Ends
