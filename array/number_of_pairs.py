'''
PROBLEM STATEMENT
-----------------
Given two arrays X and Y of positive integers, find number of pairs such that xy > yx (raised to power of) where x is an element from X and y is an element from Y.

Input:
The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. Each test consists of three lines. The first line of each test case consists of two space separated M and N denoting size of arrays X and Y respectively. The second line of each test case contains M space separated integers denoting the elements of array X. The third line of each test case contains N space separated integers denoting elements of array Y.

Output:
Corresponding to each test case, print in a new line, the number of pairs such that x^y > y^x.

Constraints:
1 ≤ T ≤ 100
1 ≤ M, N ≤ 10^5
1 ≤ X[i], Y[i] ≤ 10^3

Example:
Input
1
3 2
2 1 6
1 5

Output
3

Explanation:
Testcase 1: The pairs which follow x^y > y^x are as such: 2^1 > 1^2,  2^5 > 5^2 and 6^1 > 1^6 

LOGIC
-----
1.Brute Force Solution: Consider each element of x and y and check whether the condition satisfies or not

The time complexity is O(len(x)*len(y)).

SOURCE
------
geeksforgeeks

CODE
----
'''

def pairs(n, m, x, y):
    
    count = 0
    
    for i in range(n):
        for j in range(m):
            if pow(x[i],y[j]) > pow(y[j],x[i]):
                count += 1
                
    return count

t = int(input())
for _ in range(t):
    l = [int(x) for x in input().split()]
    n = l[0]
    m = l[1]
    x = [int(a) for a in input().split()]
    y = [int(a) for a in input().split()]
    print(pairs(n, m, x, y))
