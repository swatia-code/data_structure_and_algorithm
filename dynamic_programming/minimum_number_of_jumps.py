'''
PROBLEM STATEMENT
-----------------
Given an array of integers where each element represents the max number of steps that can be made forward from that element. The task is to find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then cannot move through that element.

Input: 
The first line contains an integer T, depicting total number of test cases.  Then following T lines contains a number n denoting the size of the array. Next line contains the sequence of integers a1, a2, ..., an.

Output:
For each testcase, in a new line, print the minimum number of jumps. If answer is not possible print "-1"(without quotes).

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
0 <= ai <= 107

Example:
Input:
2
11
1 3 5 8 9 2 6 7 6 8 9
6
1 4 3 2 6 7
Output:
3
2

Explanation:
Testcase 1: First jump from 1st element, and we jump to 2nd element with value 3. Now, from here we jump to 5h element with value 9. and from here we will jump to last.

LOGIC
-----
In this way, make a jumps[] array from left to right such that jumps[i] indicates the minimum number of jumps needed to reach arr[i] from arr[0].
To fill the jumps array run a nested loop inner loop counter is j and outer loop count is i.
Outer loop from 1 to n-1 and inner loop from 0 to n-1.
if i is less than j + arr[j] then set jumps[i] to minimum of jumps[i] and jumps[j] + 1. initially set jump[i] to INT MAX
Finally, return jumps[n-1].

Time Complexity: O(n^2)

SOURCE
------
geeksforgeeks

CODE
----
'''
def minimum_number_of_steps(n, l):
    
    jumps = [0 for i in range(n)]
    
    
    if l[0] == 0 or n == 0:
        return -1
             
    
    for i in range(1, n): 
        jumps[i] = float('inf') 
        for j in range(i): 
            if (i <= j + l[j]) and (jumps[j] != float('inf')): 
                jumps[i] = min(jumps[i], jumps[j] + 1) 
                break
            
    if jumps[n - 1] == float('inf'):
        return -1
    
    return jumps[n-1] 

t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    print(minimum_number_of_steps(n, l))
