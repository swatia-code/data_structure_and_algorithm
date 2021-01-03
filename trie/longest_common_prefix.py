"""
PROBLEM STATEMENT
-----------------
Given a array of N strings, find the longest common prefix among all strings present in the array.

Input:
The first line of the input contains an integer T which denotes the number of test cases to follow. Each test case contains an integer N. Next line has space separated N strings.

Output:
Print the longest common prefix as a string in the given array. If no such prefix exists print "-1"(without quotes).

Constraints:
1 <= T <= 103
1 <= N <= 103
1 <= |S| <= 103

Example:
Input:
2
4
geeksforgeeks geeks geek geezer
3
apple ape april

Output:
gee
ap

Explanation:
Testcase 1: Longest common prefix in all the given string is gee.


LOGIC
-----
Steps:

Insert all the words one by one in the trie. After inserting we perform a walk on the trie.
In this walk, go deeper until we find a node having more than 1 children(branching occurs) or 0 children (one of the string gets exhausted).
This is because the characters (nodes in trie) which are present in the longest common prefix must be the single child of its parent, i.e- there should not be branching in any of these nodes.
Time Complexity : Inserting all the words in the trie takes O(MN) time and performing a walk on the trie takes O(M) time, where-

N = Number of strings
M = Length of the largest string
Auxiliary Space: To store all the strings we need to allocate O(26*M*N) ~ O(MN) space for the Trie.

SOURCE
------
geeksforgeeks

CODE
----
"""
#code
ALPHABET_SIZE = 26
indexs = 0
class TrieNode: 
    def __init__(self): 
        self.isLeaf = False
        self.children = [None]*ALPHABET_SIZE 
  
def insert(key, root): 
    pCrawl = root 
    for level in range(len(key)): 
        index = ord(key[level]) - ord('a') 
        if pCrawl.children[index] == None: 
            pCrawl.children[index] = TrieNode() 
        pCrawl = pCrawl.children[index] 
    pCrawl.isLeaf = True
  
def constructTrie(arr, n, root): 
    for i in range(n): 
        insert(arr[i], root) 
  
def countChildren(node): 
    count = 0
    for i in range(ALPHABET_SIZE): 
        if node.children[i] != None: 
            count +=1
            global indexs 
            indexs = i 
    return count 
      
def walkTrie(root): 
    pCrawl = root 
    prefix = "" 
    while(countChildren(pCrawl) == 1 and pCrawl.isLeaf == False): 
        pCrawl = pCrawl.children[indexs] 
        prefix += chr(97 + indexs) 
    return prefix or -1
  
def commonPrefix(arr, n, root): 
    constructTrie(arr, n, root) 
    return walkTrie(root) 
  
t = int(input())
for _ in range(t):
    n = int(input())
    l = [x for x in input().split()]
    root = TrieNode()
    print(commonPrefix(l, n, root))
