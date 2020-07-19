'''
PROBLEM STATEMENT
-----------------
Given a binary array A of size N and an integer M. Find the maximum number of consecutive 1's produced by flipping at most M 0's.

Input:
The first line contains an integer T denoting the total number of test cases. In each test cases, the first line contains an integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.  Third line consists of an integer m that is maximum number of flips allowed.

Output:
Output the maximum numbers of consecutive 1's.

Constraints:
1 <= T <= 103
1 <= N <= 107
0 <= M <= N
0 <= Ai <= 1

Example:
Input:
1
11
1 0 0 1 1 0 1 0 1 1 1
2

Output:
8

Explanation:
Testcase 1: Maximum subarray is of size 8 which can be made subarray of all 1 after flipping two zeros to 1.

LOGIC
-----
For all positions of 0’s calculate left[] and right[] which defines the number of consecutive 1’s to the left of i and right of i respectively.

For example, for arr[] = {1, 1, 0, 1, 1, 0, 0, 1, 1, 1} and m = 1, left[2] = 2 and right[2] = 2, left[5] = 2 and right[5] = 0, left[6] = 0 and right[6] = 3.

left[] and right[] can be filled in O(n) time by traversing array once and keeping track of last seen 1 and last seen 0. While filling left[] and right[], we also store indexes of all zeroes in a third array say zeroes[]. For above example, this third array stores {2, 5, 6}

Now traverse zeroes[] and for all consecutive m entries in this array, compute the sum of 1s that can be produced. This step can be done in O(n) using left[] and right[].

An Efficient Solution can solve the problem in O(n) time and O(1) space. The idea is to use Sliding Window for the given array. The solution is taken from here.
Let us use a window covering from index wL to index wR. Let the number of zeros inside the window be zeroCount. We maintain the window with at most m zeros inside.

The main steps are:
– While zeroCount is no more than m: expand the window to the right (wR++) and update the count zeroCount.
– While zeroCount exceeds m, shrink the window from left (wL++), update zeroCount;
– Update the widest window along the way. The positions of output zeros are inside the best window.

SOURCE
------
geeksforgeeks

CODE
----
'''
def maximize_ones(l, n, m):
    left = right = 0
    window = 0
    zero_count = 0
    
    while right < n:
 
        if zero_count <= m:
            if l[right] == 0:
                zero_count += 1
            right += 1
            
        if zero_count > m:
            if l[left] == 0:
                zero_count -= 1
            left += 1
            
        if (right - left > window) and zero_count <= m:
            window = right - left
            
    return window

t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    m = int(input())
    print(maximize_ones(l, n, m))
