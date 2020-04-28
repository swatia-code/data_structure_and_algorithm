"""
PROBLEM STATEMENT
-----------------
Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, print the count of all triplets, in new line. If no such triplets can form, print "-1".

Constraints:
1 <= T <= 100
3 <= N <= 105
1 <= A[i] <= 106

Example:
Input:
2
4
1 5 3 2
3
3 2 7
Output:
2
-1

Explanation:
Testcase 1: There are 2 triplets: 1 + 2 = 3 and 3 +2 = 5

LOGIC
-----
The naive approach would take O(n3). Better if we sort the array, and then iterate.


SOURCE
------
geeksforgeeks

CODE
----
"""

def triplet(li):
    li.sort()
    count = 0
    i =len(li)-1
    while i >=0:
        sum = li[i]
        j = 0
        k = i-1
        while j<k:
            if li[j] + li[k] == sum:
                count +=1
                j += 1
                
            if li[j]+li[k]>sum:
                k -=1
                
            else:
                j+=1

        i -= 1
    if count==0:
        count = -1
    return count
        
t = int(input())
for i in range(t):
    n = input()
    l = [int(x) for x in input().split()]
    print(triplet(l))

