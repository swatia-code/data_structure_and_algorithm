'''
PROBLEM STATEMENT
-----------------
The cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.

Input: 
First line contains number of test cases T. First line of each test case contains an integer value N denoting the number of days, followed by an array of stock prices of N days. 

Output:
For each testcase, output all the days with profit in a single line. And if there is no profit then print "No Profit".

Constraints:
1 <= T <= 100
2 <= N <= 103
0 <= Ai <= 104

Example
Input:
3
7
100 180 260 310 40 535 695
4
100 50 30 20
10
23 13 25 29 33 19 34 45 65 67

Output:
(0 3) (4 6)
No Profit
(1 4) (5 9)

Explanation:
Testcase 1: We can buy stock on day 0, and sell it on 3rd day, which will give us maximum profit.

Note: Output format is as follows - (buy_day sell_day) (buy_day sell_day)
For each input, output should be in a single line.

LOGIC
-----
Find the local minima and store it as starting index. If not exists, return.
Find the local maxima. and store it as ending index. If we reach the end, set the end as ending index.
Update the solution (Increment count of buy sell pairs)
Repeat the above steps if end is not reached.

SOURCE
------
geeksforgeeks

CODE
----
'''
def stock_buy_sell(l, n):
    if n == 1:
        print('No Profit', end=" ")
        return 
    
    res = list()
    
    i = 0
    
    while i < n-1:
        # i is less than n-1 as we can't buy on last day
        
        #finding the buy day
        while (i < n - 1) and l[i + 1] <= l[i]:
            i += 1
            
        if i == n-1:
            break
        
        buy = i
        
        i += 1
        #finding sell day
        while (i < n) and  l[i - 1] <= l[i]:
            i += 1
            
        sell = i - 1
        
        res.append("({} {})".format(buy, sell))
        
    if len(res) == 0:
        print('No Profit',end=" ")
    else:
        for ele in res:
            print(ele, end=" ")
        

t = int(input())
for _ in range(t):
    size = int(input())
    l = [int(x) for x in input().split()]
    stock_buy_sell(l, size)
    print()
