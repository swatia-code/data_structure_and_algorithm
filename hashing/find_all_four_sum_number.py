"""
PROBLEM STATEMENT
-----------------
Given an array A of size N, find all combination of four elements in the array whose sum is equal to a given value K. For example, if the given array is {10, 2, 3, 4, 5, 9, 7, 8} and K = 23, one of the quadruple is “3 5 7 8” (3 + 5 + 7 + 8 = 23).

The output should contain only unique quadrples  For example, if input array is {1, 1, 1, 1, 1, 1} and K = 4, then output should be only one quadrple {1, 1, 1, 1}.

Note: Print -1 if no such quadruple is found. 
 

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two lines. The first line of input contains two integers N and K. Then in the next line are N space separated values of the array.

Output:
For each test case in a new line print all the quadruples present in the array separated by space which sums up to value of K. Each quadruple is unique which are separated by a delimeter "$" and are in increasing order.

Constraints:
1 <= T <= 100
1 <= N <= 1000
-1000 <= K <= 1000
-100 <= A[] <= 100

Example:
Input:
2
5 3
0 0 2 1 1 
7 23
10 2 3 4 5 7 8

Output:
0 0 1 2 $
2 3 8 10 $2 4 7 10 $3 5 7 8 $

LOGIC
-----
Store sums of all pairs in a hash table
Traverse through all pairs again and search for X – (current pair sum) in the hash table.
If a pair is found with the required sum, then make sure that all elements are distinct array elements and an element is not considered more than once.

SOURCE
------
geeksforgeeks

CODE
----
"""

#code
def sum_number(l, sum):
    l = sorted(l)
    m = dict()
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            m[l[i] + l[j]] = [i, j]
            
    res = list()
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            s = l[i] + l[j]
            if (sum - s) in m:
                res_list = m[sum - s]
                new_list = list()
                if i not in res_list and j not in res_list:
                    new_list.append(l[i])
                    new_list.append(l[j])
                    new_list.append(l[res_list[0]])
                    new_list.append(l[res_list[1]])
                    res.append(sorted(new_list))
                    
                    
    res = [list(t) for t in set(map(tuple, res))]
    res.sort() 
    if len(res):
        for ele in res:
            for e in ele:
                print(e, end=" ")
            print("$",end="")
    else:
        print("-1",end="")
        
    print()
                    
                    
    
t = int(input())
for _ in range(t):
    sum = [int(x) for x in input().split()][1]
    l = [int(x) for x in input().split()]
    sum_number(l, sum)
