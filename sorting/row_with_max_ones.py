'''
PROBLEM STATEMENT
-----------------
Given a boolean 2D array where each row is sorted. Find the row with the maximum number of 1s.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case contains n and m, where n is the number of rows and m is the number of columns. The second line of each test case contains the array elements.

Output:
Print the row with the maximum number of 1s.

Constraints:
1 ≤ T ≤ 50
1 ≤ n,m ≤ 103

Example:
Input:
2
4 4
0 1 1 1 0 0 1 1 1 1 1 1 0 0 0 0
2 2
0 0 1 1

Output:
2
1

Explanation :
Testcase 1 : Row 2 is having maximum number of 1s (0-based indexing).

LOGIC
-----
find the least position of one using binary search for every row

SOURCE
------
geeksforgeeks

CODE
----
'''
t=int(input())
for _ in range(t):
    k=0
 
    n,m=list(map(int,input().split()))
    a=[]
    while(len(a)<n*m):
        try:    
            a+= list(map(int,input().split()))
        except:
            break
    
    i=0
    l=[]
    while i<n*m:
        a1=a[i:i+m]
        
        l.append(a1.count(1))
        i=i+m
    
    print(l.index(max(l)))
        
    
