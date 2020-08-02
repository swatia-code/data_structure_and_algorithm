'''
PROBLEM STATEMENT
-----------------
Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details.

Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung" or "i like sam sung".

Input:
First line is integer T denoting number of test cases. 1<=T<=100.
Every test case has 3 lines.
First line is N number of words in dictionary. 1<=N<=12.
Second line contains N strings denoting the words of dictionary. Length of each word is less than 15.
Third line contains a string S of length less than 1000.

Output:
Print 1 is possible to break words, else print 0.

Example:
Input:
2
12
i like sam sung samsung mobile ice cream icecream man go mango
ilike
12
i like sam sung samsung mobile ice cream icecream man go mango
idontlike
Output:
1
0

LOGIC
-----
The idea is simple, we consider each prefix and search it in dictionary. If the prefix is present in dictionary, we recur for rest of the string (or suffix). If the recursive call for suffix returns true, we return true, otherwise we try next prefix. If we have tried all prefixes and none of them resulted in a solution, we return false.

SOURCE
------
geeksforgeeks

CODE
----
'''
def in_dictionary(word, dictionary):
    for ele in dictionary:
        if ele == word:
            return True
            
    return False

def word_break(s, dictionary):
    n = len(s)
    if n == 0:
        return True
        
    dp = [False for i in range(n + 1)]
    
    for i in range(1, n + 1):

        if dp[i] == False and in_dictionary(s[:i], dictionary):
            
            dp[i] = True
            
        if dp[i]:
            
            if i == n:
                return True
                
            for j in range(i + 1, n + 1):
                if dp[j] == False and in_dictionary(s[i: j], dictionary):
                    dp[j] = True
                
                if j == n  and dp[j]:
                    return True
                    
    return False
                

t = int(input())
for _ in range(t):
    n = int(input())
    dictionary = [x for x in input().split()]
    s = input()
    if word_break(s, dictionary):
        print('1')
    else:
        print('0')
