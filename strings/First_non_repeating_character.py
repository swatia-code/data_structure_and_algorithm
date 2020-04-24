"""
PROBLEM STATEMENT
-----------------
Given an input stream of N characters consisting only of lower case alphabets. The task is to find the first non repeating character, each time a character is inserted to the stream. If no non repeating element is found print -1.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N denoting the size of the stream. Then in the next line are x characters which are inserted to the stream.

Output:
For each test case in a new line print the first non repeating elements separated by spaces present in the stream at every instinct when a character is added to the stream, if no such element is present print -1.

Constraints:
1 <= T <= 200
1 <= N <= 500

Example:
Input:
2
4
a a b c
3
a a c

Output:
a -1 b b
a -1 c

Explanation:
Test Case 1: a a b c
The step wise first non-repeating elements are made bold:
a (print a)
a a (no non-repeating element, print -1)
a a b (print b)
a a b c (print b)
Result: a -1 b b

Test Case 2: a a c
a (print a)
a a (no non-repeating element, print -1)
a a c (print c)
Result: a -1 c

LOGIC
-----
We have take store record of first and second occurance of character. When the character occurs for the first time,we store it in dictionary and append in occur array. When the character occurs for second time, then two cases arise:
1)The charater is same as that of first non repeating character we have been printing. In this case we first have to put the value of that character as false in our dictionary and find suitable character from our queue such that it's value in dictionary is true otherwise we take non repeating character value as "-1"
2) The character is not same as that of first non repeating character constant

CODE
----
"""

def get_new_char(queue,check):
    new_char = '-1'
    for ele in queue:
        if check[ele]=="True":
            new_char = ele
            break
    return new_char

def non_repeating_char(s):
    queue = list()
    check = dict()
    
    queue.append(s[0])
    check[s[0]] = "True"
    print_char = s[0]
    print(print_char,end=" ")
    
    for i in range(1,len(s)):
        if s[i]!=' ':
            if s[i] in check:
                
                check[s[i]] = "False"
                if s[i]==print_char:
                    print_char = get_new_char(queue,check)
                print(print_char,end=" ")
                
                
            else:
                
                queue.append(s[i])
                check[s[i]] = "True"
                if print_char == "-1":
                    print_char = get_new_char(queue,check)
                print(print_char,end=" ")
            

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    non_repeating_char(s)
    print()
