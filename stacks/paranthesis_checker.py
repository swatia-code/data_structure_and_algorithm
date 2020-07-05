'''
PROBLEM STATEMENT
-----------------
Given an expression string exp. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”

Input:
The first line of input contains an integer T denoting the number of test cases.  Each test case consists of a string of expression, in a separate line.

Output:
Print 'balanced' without quotes if the pair of parenthesis is balanced else print 'not balanced' in a separate line.

Constraints:
1 ≤ T ≤ 100
1 ≤ |s| ≤ 105

Example:
Input:
3
{([])}
()
([]

Output:
balanced
balanced
not balanced

LOGIC
-----


SOURCE
------
geeksforgeeks

CODE
----
'''
def is_balanced(st):
    
    # forming a stack
    s = list()
    
    for ele in st:
        if ele == '{' or ele =='[' or ele =='(':
            s.append(ele)
        elif ele == '}':
            if len(s) == 0:
                return False
            else:
                if s[-1] != '{':
                    return False
                else:
                    s.pop()
        elif ele == ')':
            if len(s) == 0:
                return False
            else:
                if s[-1] != '(':
                    return False
                else:
                    s.pop()
        elif ele == ']':
            if len(s) == 0:
                return False
            else:
                if s[-1] != '[':
                    return False
                else:
                    s.pop()
        
                
    if len(s) == 0:
        return True
    else:
        return False

t = int(input())
for _ in range(t):
    s = input()
    if is_balanced(s):
        print('balanced')
    else:
        print('not balanced')
