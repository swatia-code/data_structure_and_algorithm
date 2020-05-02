"""
PROBLEM STATEMENT
-----------------
Given a value V. You have to make change for V cents, given that you have infinite supply of each of C{ C1, C2, .. , Cm} valued coins. Find the minimum number of coins to make the change.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is V and N, V is the value of cents and N is the number of coins. The second line of each test case contains N input C[i], value of available coins.

Output:
Print the minimum number of coins to make the change, if not possible print "-1".

Constraints:
1 ≤ T ≤ 100
1 ≤ V ≤ 106
1 ≤ N ≤ 106
1 ≤ C[i] ≤ 106

Example:
Input:
1
7 2
2 1

Output:
4

Explanation :
Testcase 1: We can use coin with value 2 three times, and coin with value 1 one times to change a total of 7.

LOGIC
-----
The minimum number of coins for a value V can be computed using below recursive formula

If V==0, then 0 coins required.
If V>0 , minCoins(Coins[0...m-1],V) = min{1+minCoins(V-coin[i]}
where i varies from 0 to m-1
and coin[i]<=V

The time complexity of recursion as we know is exponential. Since there is Overlapping subproblems, so, recomputations of same subproblem can be avaoided by constructing a Dynamic Programming based solution.

SOURCE
------
geeksforgeeks

CODE
----
"""
import sys

def minCoins(V,coins): 

	table = [0 for i in range(V + 1)] 
	table[0] = 0

	for i in range(1, V + 1): 
		table[i] = sys.maxsize 
		
	for i in range(1, V + 1): 
		for j in range(len(coins)): 
			if (coins[j] <= i): 
				sub_res = table[i - coins[j]] 
				if (sub_res != sys.maxsize and
					sub_res + 1 < table[i]): 
					table[i] = sub_res + 1
	return table[V] 


t = int(input())
for _ in range(t):
    l = [int(x) for x in input().split()]
    value = l[0]
    coins = [int(x) for x in input().split()]
    print(minCoins(value,coins))
