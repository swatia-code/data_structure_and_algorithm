'''
PROBLEM STATEMENT
-----------------
Given a string str of lowercase alphabets and an integer K, the task is to count all substrings of length K which have exactly K distinct characters.

Example:

Input: str = “abcc”, K = 2
Output: 2
Explanation:
Possible substrings of length K = 2 are
ab : 2 distinct characters
bc : 2 distinct characters
cc : 1 distinct character
Only two valid substrings exist {“ab”, “bc”}.

Input: str = “aabab”, K = 3
Output: 0
Explanation:
Possible substrings of length K = 3 are
aab : 2 distinct characters
aba : 2 distinct characters
bab : 2 distinct characters
No substrings of length 3 exists with exactly 3 distinct characters

LOGIC
-----
The idea is to use Window Sliding Technique. Maintain a window of size K and keep a count of all the characters in the window using a HashMap. Traverse through the string reducing the count of the first character of the previous window and adding the frequency of the last character of the current window in the HashMap. If the count of distinct characters in a window of length K is equal to K, increment the answer by 1.

SOURCE
------
geeksforgeeks

CODE
----	
'''
def countSubstrings(str, K):
    count = 0
    freq = dict()
    for i in range(K):
        if str[i] in freq:
            freq[str[i]] += 1
        else:
            freq[str[i]] = 1
    if len(freq) == K:
        count += 1
    start = 0
    end = K 
    while end < len(str):
        freq[str[start]] -= 1
        if freq[str[start]] == 0:
            freq.pop(str[start])
            
        if str[end] in freq:
            freq[str[end]] += 1
        else:
            freq[str[end]] = 1
        start += 1
        end += 1
        if len(freq) == K:
            count += 1
    return count
