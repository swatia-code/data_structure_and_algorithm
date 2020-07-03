'''
PROBLEM STATEMENT
-----------------
Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index ).

NOTE: Required Time Complexity O(n2).

Input:
The first line of input consists number of the testcases. The following T lines consist of a string each.

Output:
In each separate line print the longest palindrome of the string given in the respective test case.

Constraints:
1 ≤ T ≤ 100
1 ≤ Str Length ≤ 104

Example:
Input:
1
aaaabbaa

Output:
aabbaa

Explanation:
Testcase 1: The longest palindrome string present in the given string is "aabbaa".

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
def longest_palindrome(s):
    
    n = len(s)
    start = 0
    maxlength = 1
    low = 0
    high = 0
    
    for i in range(1,n):
        #for palindromes with even number of characters
        low = i - 1
        high = i
        while low >= 0 and high < n and s[low] == s[high]:
            if high - low + 1 > maxlength:
                start = low
                maxlength = high - low + 1
            low -= 1
            high += 1
            
        #for palindromes with odd number of elements
        low = i - 1
        high = i + 1
        while low >= 0 and high < n and s[low] == s[high]:
            if high - low + 1 > maxlength:
                start = low
                maxlength = high - low + 1
            low -= 1
            high += 1
            
    return s[start:start + maxlength]

def longest_palindrome_2(s):
    
    n = len(s)
    
    t = [[False for j in range(n)] for i in range(n)]
    
    #since single character is a palindrome in itself
    for i in range(n):
        t[i][i] = True
        
    maxlength = 1
    start = 0
    
    #going for palindrome for length 2
    i = 0
    # this boolean is to handle the case when multiples
    #palindromes of length 2 are there so return the first one
    first_time = True
    while i < n-1:
        if s[i] == s[i + 1]:
            maxlength = 2
            if first_time:
                start = i
                first_time = False
            t[i][i + 1] = True
        i += 1
            
    #going for palindrome substring of higher order
    k = 3
    while k <= n:
        #since size of substring cannot be larger than the string itself
        i = 0
        while i < n - k + 1:
            j = i + k - 1
            if t[i + 1][j - 1] and s[i] == s[j]:
                t[i][j] = True
                
                if k > maxlength:
                    maxlength = k
                    start = i
        
            i += 1
        k += 1
 
    return s[start:start + maxlength ]  
    

t = int(input())
for _ in range(t):
    s = input()
    print(longest_palindrome(s))
