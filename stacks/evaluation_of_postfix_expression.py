'''
PROBLEM STATEMENT
-----------------
Given a postfix expression, the task is to evaluate the expression and print the final value. Operators will only include the basic arithmetic operators like *,/,+ and - . 

Input:
The first line of input will contains an integer T denoting the no of test cases . Then T test cases follow. Each test case contains an postfix expression.

Output:
For each test case, in a new line, evaluate the postfix expression and print the value.

Constraints:
1 <= T <= 100
1 <= length of expression <= 100

Example:
Input:
2
231*+9-
123+*8-
Output:
-4
-3

Explanation: 
Test Case 1: 231*+9-
- : ( ) - ( )
9 : ( ) - (9)
+ : ( ( ) + ( ) ) - (9)
'*':  ( ( ) + ( ( ) * ( ) ) ) - (9)
1 : ( ( ) + ( ( ) * (1) ) ) - (9)
3 : ( ( ) + ( (3) * (1) ) ) - (9)
2 : ( (2) + ( (3) * (1) ) ) - (9) 
Result = (2 + 3) - 9 = 5 - 9 = -4

Test Case 2: 123+*8-
- : ( ) - ( )
8 : ( ) - (8)
* : ( ( ) * ( ) ) - (8)
+ : ( ( ) * ( ( ) + ( ) ) ) - (8)
3 : ( ( ) * ( ( ) + (3) ) ) - (8)
2 : ( ( ) * ( (2) + (3) ) ) - (8)
1 : ( (1) * ( (2) + (3) ) ) - (8) 
Result = (1 * 5) - 8 = 5 - 8 = -3

LOGIC
-----
Following is algorithm for evaluation postfix expressions.
1) Create a stack to store operands (or values).
2) Scan the given expression and do following for every scanned element.
…..a) If the element is a number, push it into the stack
…..b) If the element is a operator, pop operands for the operator from stack. Evaluate the operator and push the result back to the stack
3) When the expression is ended, the number in the stack is the final answer

SOURCE
------
geeksforgeeks

CODE
----
'''
def evaluate_postfix(s):
    stack = list()
    for ele in s:
        if ele.isdigit():
            stack.insert(0, ele)
        else:
            if len(s) < 2:
                print("String cannot be evaluated")
                return
            else:
                ele_1 = stack.pop(0)
                ele_2 = stack.pop(0)
                ele_3 = str(int(eval(ele_2 + ele + ele_1)))
                stack.insert(0, ele_3)
                
    return stack[0]
                

t = int(input())
for _ in range(t):
    s = input()
    print(evaluate_postfix(s))
