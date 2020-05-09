"""
PROBLEM STATEMENT
-----------------
Given an array of words, print the count of all anagrams together in sorted order (increasing order of counts).
For example, if the given array is {“cat”, “dog”, “tac”, “god”, “act”}, then grouped anagrams are “(dog, god) (cat, tac, act)”. So the output will be 2 3.

Input:
First line consists of T test case. First line of every test case consists of N, denoting the number of words in array. Second line of every test case consists of words of array.

Output:
Single line output, print the counts of anagrams in increasing order.

Constraints:
1<=T<=100
1<=N<=50

Example:
Input:
2
5
act cat tac god dog
3
act cat tac
Output:
2 3
3

LOGIC
-----
Simple use of sorting and dictionary.

SOURCE
------
geeksforgeeks

CODE
----
"""
#code
def anagrams(l):
    res = []
    
    li = dict()
    for ele in l:
        lis = [s for s in ele]
        lis.sort()
      
        s = ""
        for ele in lis:
            s += ele
            
        if s not in li:
            li[s] = 1
        else:
            li[s] += 1
            
    li = sorted(li.items(), key=lambda x: x[1])
    for ele in li:
        print(ele[1],end=" ")
    
    print()
        
    
    
t = int(input())
for _ in range(t):
    n = int(input())
    l = [x for x in input().split()]
    anagrams(l)
