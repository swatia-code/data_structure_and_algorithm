"""
PROBLEM STATEMENT
-----------------
Given a Binary Tree find the length of the longest path which comprises of nodes with consecutive values in increasing order. Every node is considered as a path of length 1.

LOGIC
-----
If current node has value more than it's parent node then it makes a consecutive path, at each node we will compare node's value with it's parent value and update the longest consecutive path accordingly.

SOURCE
------
geeksforgeeks

CODE
---
"""
class newNode: 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = None

def longestConsecutiveUtil(root, curLength, 
						expected, res): 
	if (root == None): 
		return

	if (root.data == expected): 
		curLength += 1
	else: 
		curLength = 1

	res[0] = max(res[0], curLength) 

	longestConsecutiveUtil(root.left, curLength, 
						root.data + 1, res) 
	longestConsecutiveUtil(root.right, curLength, 
						root.data + 1, res) 

def longestConsecutive(root): 
	if (root == None): 
		return 0

	res = [0] 

	longestConsecutiveUtil(root, 0, root.data, res) 

	return res[0] 

if __name__ == '__main__': 

	root = newNode(6) 
	root.right = newNode(9) 
	root.right.left = newNode(7) 
	root.right.right = newNode(10) 
	root.right.right.right = newNode(11) 

	print(longestConsecutive(root)) 

