'''
PROBLEM STATEMENT
-----------------
You are given a string S of alphabet characters and the task is to find its matching decimal representation as on the shown keypad. Output the decimal representation corresponding to the string. For example: if you are given “amazon” then its corresponding decimal representation will be 262966.



Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of a single line containing a string.

Output:
For each test case, print in a new line, the corresponding decimal representation of the given string.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Note: N = |S|.

Constraints:
1 ≤ T ≤ 100
1 ≤ length of String ≤ 100

Example:
Input:
2
geeksforgeeks
geeksquiz
Output:
4335736743357
433577849

Explanation:
Testcase 1: In geekforgeeks, decimal representation for g is 4, e is 3, k is 5, s is 7 and so on. Hence the output for the given input will be 4335736743357.
Testcase 2: In geeksquiz, decimal representation for g is 4, e is 3, k is 5, s is 7, q is 7, u is 8, i is 4 and z is 9. Hence, output for the given input will be 433577849.

LOGIC
-----
Simple use of hastable

SOURCE
------
geeksforgeeks

CODE
----
'''
keypad = {'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3', 'g': '4', 'h': '4', 'i': '4', 'j': '5', 'k': '5', 'l': '5', 'm': '6', 'n': '6', 'o': '6', 'p': '7', 'q': '7', 'r': '7', 's': '7', 't': '8', 'u': '8', 'v': '8', 'w': '9', 'x': '9', 'y': '9', 'z': '9'}

def keypad_typing(s):
    res = ''
    for ele in s:
        val = keypad[ele]
        res = res + val
        
    return res
    
t = int(input())
for _ in range(t):
    s = input()
    print(keypad_typing(s))
