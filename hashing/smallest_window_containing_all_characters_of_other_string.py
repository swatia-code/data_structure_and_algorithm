'''
PROBLEM STATEMENT
-----------------
Given a string S and text T. Output the smallest window in the string S having all characters of the text T. Both the string S and text T contains lowercase english alphabets.

Input:
First line of the input contains an integer T, denoting the number of test cases. Then T test case follows. Each test contains 2 lines having a string S and next line contains text T.

Output:
Output the smallest window of the string containing all the characters of the text. If such window doesn`t exist or this task can not be done then print -1.

Constraints:
1 <= T <= 100
1 <= |N|, |X| <= 1000

Example:
Input:
2
timetopractice
toc
zoomlazapzo
oza

Output:
toprac
apzo

Explanation:
Testcase 1: "toprac" is the smallest substring in the given string S which contains every characters of T.

LOGIC
-----
First check if the length of string is less than the length of the given pattern, if yes then “no such window can exist “.
Store the occurrence of characters of the given pattern in a hash_pat[].
Start matching the characters of pattern with the characters of string i.e. increment count if a character matches.
Check if (count == length of pattern ) this means a window is found.
If such window found, try to minimize it by removing extra characters from the beginning of the current window.
Update min_length.
Print the minimum length window.


SOURCE
------
geeksforgeeks

CODE
----
'''
def smallest_window(st, pat):
    st_len = len(st)
    pat_len = len(pat)
    
    if pat_len > st_len:
        return "-1"
        
    hash_pat = dict()
    hash_st = dict()
    
    for ele in pat:
        if ele not in hash_pat:
            hash_pat[ele] = 1
        else:
            hash_pat[ele] += 1
            
    start = 0
    start_ind = -1
    count = 0
    min_len = st_len
    
    
    for i in range(len(st)):
        
        if st[i] not in hash_st:
            hash_st[st[i]] = 1
        else:
            hash_st[st[i]] += 1
            
        if st[i] in hash_pat and hash_st[st[i]] <= hash_pat[st[i]]:
            count += 1
            
        if count == pat_len:
            
            while (st[start] in hash_pat and hash_st[st[start]] > hash_pat[st[start]]) or st[start] not in hash_pat:
                if (st[start] in hash_pat and hash_st[st[start]] > hash_pat[st[start]]) or st[start] not in hash_pat:
                    hash_st[st[start]] -= 1
                    
                start += 1
                
            window = i - start + 1
            if min_len > window:
                min_len = window 
                start_ind = start
                
                
    if start_ind == -1:
        return "-1"
        
    return st[start_ind:start_ind+min_len]
    
t = int(input())
for _ in range(t):
    st = input()
    pat = input()
    print(smallest_window(st, pat))
