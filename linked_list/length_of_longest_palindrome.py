"""
PROBLEM STATEMENT
-----------------
Given a linked list, the task is to complete the function maxPalindrome() which returns an integer denoting  the length of
the longest palindrome list that exist in the given linked list.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line
of each test case contains an integer N denoting the size of the linked list . Then in the next line are N space separated
values of the given linked list.

Output:
For each test case output will be the required max length of the palindrome present in the given linked list.

User Task:
The task is to complete the function maxPalindrome() which should count the length of longest palindrome in the given list
and return it.

Constraints:
1 <= T <= 100
1 <= N <= 100

Example:
Input:
2
7
2 3 7 3 2 12 24
5
12 4 4 3 14

Output:
5
2

Explanation:
Testcase 1: 2 -> 3 -> 7 -> 3 -> 2 is the linked list whose nodes leads to a palindrome as 2 3 7 3 2.
 
LOGIC
-----
The idea is based on iterative linked list reverse process. We iterate through given linked list and one by one reverse every
prefix of linked list from left. After reversing a prefix, we find the longest common list beginning from reversed prefix and 
list after the reversed prefix.

TIME COMPLEXITY
---------------
O(N ^ 2)

CODE
----
"""
'''
class node:
    def __init__(self):
        self.data = None
        self.next = Non
'''
def pal_len(a, b):
    res = 0
    
    while a and b:
        if a.data != b.data:
            break
        
        res += 1
        a = a.next
        b = b.next
        
    return res
            

def maxPalindrome(head):
    # Code here
    res = 0
    prev = None
    curr = head
    
    while curr:
        n = curr.next
        curr.next = prev
        
        #checking for odd length
        res = max(res, 2 * pal_len(prev, n) + 1)

        #checking for even length
        res = max(res, 2 * pal_len(curr, n))
        
        prev = curr
        curr = n
        
    return res
