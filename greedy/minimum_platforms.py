'''
PROBLEM STATEMENT
-----------------
Given arrival and departure times of all trains that reach a railway station. Your task is to find the minimum number of platforms required for the railway station so that no train waits.

Note: Consider that all the trains arrive on the same day and leave on the same day. Also, arrival and departure times will not be same for a train, but we can have arrival time of one train equal to departure of the other. In such cases, we need different platforms, i.e at any given instance of time, same platform can not be used for both departure of a train and arrival of another.

Input:
The first line of input contains T, the number of test cases. For each test case, first line will contain an integer N, the number of trains. Next two lines will consist of N space separated time intervals denoting arrival and departure times respectively.
Note: Time intervals are in the 24-hour format(hhmm),  of the for HHMM , where the first two charcters represent hour (between 00 to 23 ) and last two characters represent minutes (between 00 to 59).

Output:
For each test case, print the minimum number of platforms required for the trains to arrive and depart safely.

Constraints:
1 <= T <= 100
1 <= N <= 1000
1 <= A[i] < D[i] <= 2359

Example:
Input:
2
6 
0900  0940 0950  1100 1500 1800
0910 1200 1120 1130 1900 2000
3
0900 1100 1235
1000 1200 1240 

Output:
3
1

Explanation:
Testcase 1: Minimum 3 platforms are required to safely arrive and depart all trains.

LOGIC
-----
Sort the arrival and departure time of trains.
Create two pointers i=0, and j=0 and a variable to store ans and current count plat
Run a loop while i<n and j<n and compare the ith element of arrival array and jth element of departure array.
if the arrival time is less than or equal to departure then one more platform is needed so increase the count, i.e. plat++ and increment i
Else if the arrival time greater than departure then one less platform is needed so decrease the count, i.e. plat++ and increment j
Update the ans, i.e ans = max(ans, plat).

SOURCE
------
geeksforgeeks

CODE
----
'''
def min_platform(arr, dept):
    temp = 0
    res = 0
    i = 0
    j = 0
    
    arr.sort()
    dept.sort()
    
    while i < n and j < n:
        if arr[i] <= dept[j]:
            temp += 1
            i += 1
            
        elif arr[i] > dept[j]:
            temp -= 1
            j += 1
            
        if temp > res:
            res = temp
            
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    dept = [int(x) for x in input().split()]
    print(min_platform(arr, dept))
