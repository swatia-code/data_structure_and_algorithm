'''
PROBLEM STATEMENT
-----------------
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate the span of stock’s price for all n days. 
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, N is the size of the array. The second line of each test case contains N input C[i].

Output:
For each testcase, print the span values for all days.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 200
1 ≤ C[i] ≤ 800

Example:
Input:
2
7
100 80 60 70 60 75 85
6
10 4 5 90 120 80

Output:
1 1 1 2 1 4 6
1 1 2 4 5 1

LOGIC
-----
We see that S[i] on day i can be easily computed if we know the closest day preceding i, such that the price is greater than on that day than the price on the day i. If such a day exists, let’s call it h(i), otherwise, we define h(i) = -1.
To implement this logic, we use a stack as an abstract data type to store the days i, h(i), h(h(i)), and so on. When we go from day i-1 to i, we pop the days when the price of the stock was less than or equal to price[i] and then push the value of day i back into the stack.

SOURCE
------
geeksforgeeks

CODE
----
'''
def stock_span_helper(n, price, S):
    st = list()
    st.append(0)
    
    S[0] = 1
    
    for i in range(1, n):
        while len(st) > 0 and price[st[-1]] <= price[i]:
            st.pop()
            
        S[i] = i + 1 if len(st) <= 0 else (i - st[-1])
        
        st.append(i)
        

def stock_span_problem(n, price):
    S = [0] * n
    stock_span_helper(n, price, S)
    
    for i in range(n):
        print(S[i], end=" ")
        
    print()

t = int(input())
for _ in range(t):
    n = int(input())
    price = [int(x) for x in input().split()]
    stock_span_problem(n, price)
