'''
PROBLEM STATEMENT
-----------------
Given a string str and another string patt. Find the character in patt that is present at the minimum index in str. If no character of patt is present in str then print ‘No character present’.

Input:
The first line of input contains an integer T denoting the number of test cases. Then the description of T test cases follow. Each test case contains two strings str and patt respectively.

Output:
Output the character in patt that is present at the minimum index in str. Print "$" (without quotes) if no character of patt is present in str.

Constraints:
1 <= T <= 105
1 <= |str|, |patt| <= 105

Example:
Input:
2
geeksforgeeks
set
adcffaet
onkl

Output:
e
$

Explanation:
Testcase 1: e is the character which is present in given patt "geeksforgeeks" and is first found in str "set".

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
import sys
def minimum_index(s, patt):
    
    freq = dict()
    for i in range(len(s)):
        if s[i] not in freq:
            freq[s[i]] = i
    
    index = sys.maxsize
    for i in range(len(patt)):
        if patt[i] in freq:
            index = min(index, freq[patt[i]])
            
    if index != sys.maxsize:
        print(s[index])
    else:
        print('$')

t = int(input())
for _ in range(t):
    s = input()
    patt = input()
    minimum_index(s, patt)
