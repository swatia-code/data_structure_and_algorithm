"""
PROBLEM
-------

Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is S.

Output:

Print the minimum number of characters.

Constraints:

1 ≤ T ≤ 50
1 ≤ S ≤ 40

Example:

Input:
3
abcd
aba
geeks

Output:
3
0
3


LOGIC
-----
We can have a recusive solution to this problem. Let the input string be str[l...h]. The problem can be broken down into three parts:
1. Find the minimum number of insertions in substrings in the substring str[l+1....h].
2. Find the minimum number of insertions in substrings in the substring str[l...h-1]
3. Find the minimum number of insertions in substrings in the substring str[l+1..h-1].

Base case here is : if l>h we should return maximum value as start can not be greater than end of string. If l==h i.e. if start is equal to end then we have string with only one character which is a palindrome in itself, so return 0 as we don't need any more characters to make it a palindrome. Moreover, if l==h-1 and str[l]==str[h], then also we need to return 0 as we have string of two characters which are same i.e. again a palindrome otherwise, we need to return 1, as we need one more character to make it a palindrome.

Recursive step here is:
If str[l]==str[h] then we find min number of insertions in substring str[l+1.. h-1] otherwise it would be minimum of min number of insertions in substrings str[l+1...h] and str[l...h-1] incremented by one.


CODE
----
"""

#code
import sys
def form_palindrome(str,l,h):
    #base case
    if l>h:
        return sys.maxsize
        
    if l == h:
        return 0
        
    if l == h-1 :
        return 0 if str[l]==str[h] else 1
        
    #recursion step
    if str[l]==str[h]:
        return form_palindrome(str,l+1,h-1)
    else:
        return min(form_palindrome(str,l+1,h),form_palindrome(str,l,h-1))+1
        

t = int(input())

for _ in range(t):
    s = input()
    print(form_palindrome(s,0,len(s)-1))
