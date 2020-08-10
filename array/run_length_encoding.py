'''
PROBLEM STATEMENT
-----------------
Given a string, Your task is to  complete the function encode that returns the run length encoded string for the given string.
eg if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6″.
You are required to complete the function encode that takes only one argument the string which is to be encoded and returns the encoded string.


Input:
The first line contains T denoting no of test cases . Then T test cases follow . Each test case contains a string str which is to be encoded .

Output:
For each test case output in a single line the so encoded string .

Your Task:
Complete the function encode() which takes a character array as a input parameter and returns the encoded string.

Expected Time Complexity: O(N), N = length of given string.
Expected Auxiliary Space: O(1)

Constraints:
1<=T<=100
1<=length of str<=100

Example:
Input(To be used only for expected output)
2
aaaabbbccc
abbbcdddd

Output
a4b3c3
a1b3c1d4

Explanation:
Test Case 1: a repeated 4 times consecutively, b 3 times, c also 3 times.
Test Case 2: a, b, c, d repeated consecutively 1, 3, 1, 4 respectively.

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
def encode(arr):
    # Code here
    
    l = list()
    ch = arr[0]
    l.append(ch)
    sum = 0
    for ele in arr:
        if ele == ch:
            sum += 1
        else:
            l.append(sum)
            l.append(ele)
            ch = ele
            sum = 1
    l.append(sum)
    return ''.join(str(ele) for ele in l)

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
