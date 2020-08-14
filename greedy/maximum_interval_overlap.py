'''
PROBLEM STATEMENT
-----------------
Consider a big party where a log register for guest’s entry and exit times is maintained. Find the time at which there are maximum guests at the party. Note that entries in the register are not in any order.  if two events have the same time, then arrival is preferred over the exit.



Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the entry and exit array. Then the next two lines contains the entry and exit array respectively.

Output:
Print the maximum no of guests and the time at which there are maximum guests at the party.

Constraints:
1<=T<=10^5
1<=N<=10^5
1<=entry[i],exit[i]<=10^5

Example:
Input:
2
5
1 2 10 5 5
4 5 12 9 12
7
13 28 29 14 40 17 3 
107 95 111 105 70 127 74 

Output:
3 5
7 40

LOGIC
-----
Similar to maximum platform problem. 
1. Keep two indexes i and j for arrival and departure array respectively.
2. Take two variables to store local max and global max and one variable to store interval
3. Sort both arrays
4. while i and j both are less than the length of array, iterate while checking 
if the arrival interval is less than the departure index. In this case update the local max and global max and interval otherwise not

SOURCE
------
geeksforgeeks

CODE
----
'''
def maximum_interval_overlap(n, arr, dept):
    '''Function to find interval at which maximum
    number of guests will be there'''
    i = 0
    j = 0
    
    current = 0
    interval = -1
    ans = 0
    
    arr.sort()
    dept.sort()
    
    while i < n and j < n:
        if arr[i] <= dept[j]:
            current += 1
            if current > ans:
                ans = current
                interval = arr[i]
            i += 1
        else:
            current -= 1
            j += 1
            
    return ans, interval

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    dept = [int(x) for x in input().split()]
    ans, interval = maximum_interval_overlap(n, arr, dept)
    print(ans, interval)
