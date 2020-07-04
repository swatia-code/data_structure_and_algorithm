'''
PROBLEM STATEMENT
-----------------
A top secret message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
You are an FBI agent. You have to determine the total number of ways that message can be decoded.
Note: An empty digit sequence is considered to have one decoding. It may be assumed that the input contains valid digits from 0 to 9 and If there are leading 0’s, extra trailing 0’s and two or more consecutive 0’s then it is an invalid string.

Example :
Given encoded message "123",  it could be decoded as "ABC" (1 2 3) or "LC" (12 3) or "AW"(1 23).
So total ways are 3.

Input:
First line contains the test cases T.  1<=T<=1000
Each test case have two lines
First is length of string N.  1<=N<=40
Second line is string S of digits from '0' to '9' of N length.

Example:
Input:
2
3
123
4
2563
Output:
3
2

LOGIC
-----
1) Initialise an array of length n+1.

2) BASE CASES:
dp[0] = 1; //1 way to decode an empty string.
dp[1] = 1; //1 way to decode a string of length 1.

3) Iterate from 2 -> n

4) WE CONSIDER TWO DIGITS AT A TIME.(LAST AND 2ND LAST DIGIT)
FIRST, WE MAKE SURE THAT THE LAST DIGIT IS NOT '0' AS EXTRA TRAILING ZEROES ARE NOT ALLOWED.
SECOND, WE MAKE SURE THAT THE TWO DIGITS FORM A VALID CHAR -> TOGETHER THEY SHOULD BE LESS THAN 27. (So 2nd last digit can be 1 or 2 and last digit should be less than 7.

5) return dp[n]

SOURCE
------
geeksforgeeks

CODE
----
'''
def total_decoding_messages(s, n):
    
    if s[0] == '0':
        return 0
    
    l = list()
    for i in range(n+1):
        l.append(0)
        
    #there is only one way to decode stringof length 0 and 1
    l[0] = 1
    l[1] = 1
    
    for i in range(2, n + 1):
        
        #checking for last element
        if s[i - 1] > '0':
            l[i] = l[i - 1]
            
        if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] < '7'):
            l[i] += l[i - 2]
            
            
    return l[n]

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(total_decoding_messages(s, n))
