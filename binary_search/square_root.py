'''
PROBLEM STATEMENT
-----------------
Given a number N, the task is to find the square root of N without using sqrt() function.

LOGIC
-----
Start iterating from i = 1. If i * i = n, then print i as n is a perfect square whose square root is i.
Else find the smallest i for which i * i is strictly greater than n.
Now we know square root of n lies in the interval i – 1 and i and we can use Binary Search algorithm to find the square root.
Find mid of i – 1 and i and compare mid * mid with n, with precision upto 5 decimal places.
If mid * mid = n then return mid.
If mid * mid < n then recur for the second half.
If mid * mid > n then recur for the first half.

SOURCE
------
geeksforgeeks

CODE
----
'''
import math 
def Square(n, i, j): 

	mid = (i + j) / 2; 
	mul = mid * mid; 

	if ((mul == n) or (abs(mul - n) < 0.00001)): 
		return mid; 

	elif (mul < n): 
		return Square(n, mid, j); 

	else: 
		return Square(n, i, mid); 

def findSqrt(n): 
	i = 1; 

	found = False; 
	while (found == False): 

		if (i * i == n): 
			print(i); 
			found = True; 
		
		elif (i * i > n): 

			res = Square(n, i - 1, i); 
			print ("{0:.5f}".format(res)) 
			found = True
		i += 1; 

t = int(input())
for _ in range(t):
  n = int(input())
  findSqrt(n)
