"""
PROBLEM STATEMENT
-----------------
Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case first line contains N(size of array). The subsequent line contains N-1 array elements.

Output:
Print the missing number in array.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
1 ≤ C[i] ≤ 107

Example:
Input:
2
5
1 2 3 5
10
1 2 3 4 5 6 7 8 10

Output:
4
9

Explanation:
Testcase 1: Given array : 1 2 3 5. Missing element is 4.

LOGIC 
-----
1. The length of the array is n-1. So the sum of all n elements, i.e. sum of numbers from 1 to n can be calculated using the formula n*(n+1)/2. Now find the sum of all the elements in the array and subtract it from the sum of first n natural numbers, it will be the value of the missing element.

2. XOR method 


SOURCE
------
geeksforgeeks

CODE
----
"""
#code
def missing_num(li,sum):
    for ele in li:
        sum -= ele
        
    return sum
    
def missing_number_2(li):
    sum_1 = 1
    sum_2 = li[0]
    for i in range(2,n+1):
        sum_1 = sum_1^i
        
    for i in range(1,len(li)):
        sum_2 = sum_2^li[i]
        
    return sum_1^sum_2

t = int(input())
for i in range(t):
    n = int(input())
    li = [int(x) for x in input().split()]
    sum = (n*(n+1))//2
    print(missing_number_2(li))
