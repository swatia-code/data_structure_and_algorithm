'''
PROBLEM STATEMENT
-----------------
Given a string S, split the given string into as many substrings as possible such that each character from the given string appears in a single substring and print all these possible parts. The task is to print those substrings.

Examples:

Input: S = “ababcbacadefegdehijhklij” 
Output: 
ababcbaca defegde hijhklij 
Explanation: 
a, b, c are only present in the first string. 
d, e, f, g are only present in the second string. 
h, i, j, k, l are only present in the third string.

Input: S = “acbbcc” 
Output: 
a cbbcc 
Explanation: 
a are only present in the first string. 
b, c are only present in the second string.

LOGIC
-----

Store the last index of occurrence of all characters in the string.
Since the string contains only lowercase letters, simply use an array of fixed size 26 to store the last indices of each character.
Initialize an empty string ans = “” and iterate over the given string and follow the steps below: 
Add the current character to the string ans if the last position of the character is more than the current index and increase the length of the partition.
If the last position of the current character is equal to the current index, then print the current string stored in ans and initialize ans to “” for storing the next partition of the string.


SOURCE
------
geeksforgeeks

CODE
----
'''
def print_substring(s):
    freq = dict()
    #storing last occurence of character 
    for i, ele in enumerate(s):
        if ele in freq:
            freq[ele] = i
        else:
            freq[ele] = i
    print(freq)
    min_pos = -1
    ans = ""
    for i, ele in enumerate(s):
        lp = freq[ele]
        min_pos = max(min_pos, lp)
        if (i == min_pos):
            ans = ans + ele
            print(ans, end=" ")
            ans = ""
            min_pos = -1
        else:
            ans = ans + ele

