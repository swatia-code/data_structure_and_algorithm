'''
PROBLEM STATEMENT
-----------------
Find and print the uncommon characters of the two given strings S1 and S2. Here uncommon character means that either the character is present in one string or it is present in other string but not in both. The strings contains only lowercase characters and can contain duplicates.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two strings in two subsequent lines.

Output:
For each testcase, in a new line, print the uncommon characters of the two given strings in sorted order.

Constraints:
1 <= T <= 100
1 <= |S1|, |S2| <= 105

Example:
Input:
1
characters
alphabets
Output:
bclpr

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
def uncommon_characters(s1, s2):
    freq1 = dict()
    freq2 = dict()
    
    for ele in s1:
        if ele not in freq1:
            freq1[ele] = True
            
    for ele in s2:
        if ele not in freq2:
            freq2[ele] = True
            
    res = ''
    for ele in freq1:
        if ele not in freq2:
            res = res+ele
        else:
            freq1[ele] = False
            freq2[ele] = False
            
    for ele in freq2:
        if freq2[ele]:
            res = res+ ele
     
    s = ''.join(sorted(res))
  
    return s

t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()
    print(uncommon_characters(s1, s2))







