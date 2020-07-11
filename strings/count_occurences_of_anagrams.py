'''
PROBLEM STATEMENT
-----------------
Given a word S and a text C. Return the count of the occurences of anagrams of the word in the text.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a text S consisting of only lowercase characters.
The second line contains a word consisting of only lowercase characters.

Output:
Print the count of the occurences of anagrams of the word C in the text S.

Constraints:
1 <= T <= 50
1 <= |S| <= |C| <= 50

Example:
Input:
2
forxxorfxdofr
for
aabaabaa
aaba

Output:
3
4

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
#code
def anagrams(s, c):
    if len(c) > len(s):
        return 0
    temp = "".join(sorted(c))
    count = 0
    for i in range(0, len(s) - len(c) + 1):
        st = "".join(sorted(s[i: i + len(c)]))
        if st == temp:
            count += 1
    
    print(count)
    
t = int(input())
for _ in range(t):
    s = input()
    c = input()
    anagrams(s,c)
