'''
PROBLEM STATEMENT
-----------------
Given an integer N, how many structurally unique binary search trees are there that store values 1...N?

Input:
First line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains a single line of input containing N.

Ouput:
For each testcase, in a new line, print the answer.

Constraints:
1<=T<=15
1<=N<=11

Example:
Input:
2
2
3
Output:
2
5

Explanation:

Testcase1:
for N = 2, there are 2 unique BSTs
     1               2  
      \            /
       2         1

Testcase2:
for N = 3, there are 5 possible BSTs
  1              3        3         2      1
    \           /        /           /    \      \
     3        2         1        1    3      2
    /       /                \                      \
   2      1               2                        3

LOGIC
-----
Total number of possible Binary Search Trees with n different keys (countBST(n)) = Catalan number Cn = (2n)! / ((n + 1)! * n!)
For n = 0, 1, 2, 3, … values of Catalan numbers are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …. So are numbers of Binary Search Trees.

Total number of possible Binary Trees with n different keys (countBT(n)) = countBST(n) * n!

Consider all possible binary search trees with each element at the root. If there are n nodes, then for each choice of root node, there are n – 1 non-root nodes and these non-root nodes must be partitioned into those that are less than a chosen root and those that are greater than the chosen root.

Let’s say node i is chosen to be the root. Then there are i – 1 nodes smaller than i and n – i nodes bigger than i. For each of these two sets of nodes, there is a certain number of possible subtrees.

Let t(n) be the total number of BSTs with n nodes. The total number of BSTs with i at the root is t(i – 1) t(n – i). The two terms are multiplied together because the arrangements in the left and right subtrees are independent. That is, for each arrangement in the left tree and for each arrangement in the right tree, you get one BST with i at the root.

Summing over i gives the total number of binary search trees with n nodes.

 t(n) = \sum_{i=1}^{n} t(i-1) t(n-i) 

The base case is t(0) = 1 and t(1) = 1, i.e. there is one empty BST and there is one BST with one node.

            t(2) = t(0)t(1) + t(1)t(0) = 2                             

            t(3) =t(0)t(2) +t(1)t(1) + t(2)t(0) = 2+1+2 = 5               

            t(4) = t(0)t(3) + t(1)t(2) +t(2)t(1)+ t(3)t(0) = 5+2+2+5 = 14                   

Also, the relationship countBT(n) = countBST(n) * n! holds. As for every possible BST, there can have n! binary trees where n is the number of nodes in BST.

SOURCE
------
geeksforgeeks

CODE
----
'''
def catalan(n, k):
    if (k > n - k):
        k = n - k
    
    res = 1
    
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
        
    return res

def unique_bst(n):
    cat = catalan(2 * n, n)
    
    return cat // (n + 1)

t = int(input())
for _ in range(t):
    n = int(input())
    print(unique_bst(n))
