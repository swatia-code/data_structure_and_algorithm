'''
PROBLEM STATEMENT
-----------------
Given two arrays of integers, write a program to check if a pair of values (one value from each array) exists such that swapping the elements of the pair will make the sum of two arrays equal.

Input:
First line of input contains a single integer T which denotes the number of test cases. T test cases follows. First line of each test case contains two space separated integers N and M. Second line of each test case contains N space separated integers denoting the elements of first array. Third line of each test case contains M space separated integers denoting the elements of second array.

Output:
For each test case, print 1 if there exists any such pair otherwise print -1.

Constraints:
1 <= T <= 100
1 <= N <= 104
1 <= M <= 104
0 <= elements <= 104

Example:
Input:
2
6 4
4 1 2 1 1 2
3 6 3 3
4 4
5 7 4 6
1 2 3 8

Output:
1
1

Explanation:
Testcase 1: 1 and 3 are two such values one from first array other from second one, if we swap these two values then we will get both arrays sum as equal.

LOGIC
-----
Sort the arrays.
Traverse both array simultaneously and do following for every pair.
If the difference is too small then, make it bigger by moving ‘a’ to a bigger value.
If it is too big then, make it smaller by moving b to a bigger value.
If it’s just right, return this pair.

SOURCE
------
geeksforgeeks

CODE
----
'''

#code
def is_sum_equal(l1, l2):
    sum_1 = sum_2 = 0
    for ele in l1:
        sum_1 += ele
        
    for ele in l2:
        sum_2 += ele
        
    l1.sort()
    l2.sort()
    
    i = 0
    j = 0
    
    
    sum = (sum_1 - sum_2) // 2
    while i<len(l1) and j<len(l2):
        
        if l1[i] - l2[j] > sum:
            j += 1
            
        elif l1[i] - l2[j] < sum:
            i += 1
            
        else:
            return True
            
    return False

t = int(input())
for _ in range(t):
    size = [int(x) for x in input().split()]
    l1 = [int(x) for x in input().split()]
    l2 = [int(x) for x in input().split()]
    if is_sum_equal(l1, l2):
        print('1')
    else:
        print('-1')
