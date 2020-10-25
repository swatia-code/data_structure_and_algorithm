'''
PROBLEM STATEMENT
-----------------
You are given an array A of size N. The array contains integers and is of even length. The elements of the array represent N coin of values V1, V2, ....Vn. You play against an opponent in an alternating way.

In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin.

You need to determine the maximum possible amouint of money you can win if you go first.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two lines of input. The first line contains N denoting the size of the array. The second line contains N elements of the array.

Output:
For each testcase, in a new line, print the maximum amout.

Constraints:
1 <= T <= 100
2 <= N <= 100
1 <= Ai <= 106

Examples:
Input:
2
4
5 3 7 10
4
8 15 3 7
Output:
15
22

Explanation:
Testcase1: The user collects maximum value as 15(10 + 5)
Testcase2: The user collects maximum value as 22(7 + 15)

LOGIC
------
Consider a row of n coins of values v1 . . . vn, where n is even. We play a game against an opponent by alternating turns. In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin. Determine the maximum possible amount of money we can definitely win if we move first.

Note: The opponent is as clever as the user.

Let us understand the problem with few examples:

5, 3, 7, 10 : The user collects maximum value as 15(10 + 5)
8, 15, 3, 7 : The user collects maximum value as 22(7 + 15)
Does choosing the best at each move gives an optimal solution? No.
In the second example, this is how the game can be finished:

…….User chooses 8.
…….Opponent chooses 15.
…….User chooses 7.
…….Opponent chooses 3.
Total value collected by user is 15(8 + 7)
…….User chooses 7.
…….Opponent chooses 8.
…….User chooses 15.
…….Opponent chooses 3.
Total value collected by user is 22(7 + 15)
So if the user follows the second game state, the maximum value can be collected although the first move is not the best.

Approach: As both the players are equally strong, both will try to reduce the possibility of winning of each other. Now let’s see how the opponent can achieve this.

There are two choices:

The user chooses the ‘ith’ coin with value ‘Vi’: The opponent either chooses (i+1)th coin or jth coin. The opponent intends to choose the coin which leaves the user with minimum value.
i.e. The user can collect the value Vi + min(F(i+2, j), F(i+1, j-1) ).
The user chooses the ‘jth’ coin with value ‘Vj’: The opponent either chooses ‘ith’ coin or ‘(j-1)th’ coin. The opponent intends to choose the coin which leaves the user with minimum value, i.e. the user can collect the value Vj + min(F(i+1, j-1), F(i, j-2) ).
Following is the recursive solution that is based on the above two choices. We take a maximum of two choices.

F(i, j) represents the maximum value the user
can collect from i'th coin to j'th coin.

F(i, j) = Max(Vi + min(F(i+2, j), F(i+1, j-1) ), 
              Vj + min(F(i+1, j-1), F(i, j-2) ))
As user wants to maximise the number of coins. 

Base Cases
    F(i, j) = Vi           If j == i
    F(i, j) = max(Vi, Vj)  If j == i + 1


SOURCE
------
geeksforgeeks

CODE
----
'''
#code
def optimalStrategyOfGame(arr, n): 

	table = [[0 for i in range(n)] 
				for i in range(n)] 
				
	for gap in range(n): 
		for j in range(gap, n): 
			i = j - gap 
			
			x = 0
			if((i + 2) <= j): 
				x = table[i + 2][j] 
			y = 0
			if((i + 1) <= (j - 1)): 
				y = table[i + 1][j - 1] 
			z = 0
			if(i <= (j - 2)): 
				z = table[i][j - 2] 
			table[i][j] = max(arr[i] + min(x, y), 
							arr[j] + min(y, z)) 
	return table[0][n - 1] 

t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    print(optimalStrategyOfGame(l, n))
