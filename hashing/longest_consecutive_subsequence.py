'''
PROBLEM STATEMENT
-----------------
Given an array arr[] of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.

Input:
The first line of input contains T, number of test cases. First line of line each test case contains a single integer N.
Next line contains N integer array.

Output:
Print the output of each test case in a seprate line.

Constraints:
1 <= T <= 100
1 <= N <= 105
0 <= a[i] <= 105

Example:
Input:
2
7
2 6 1 9 4 5 3
7
1 9 3 10 4 20 2

Output:
6
4

Explanation:
Testcase 1:  The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.

Testcase2: 1, 2, 3, 4 is the longest consecutive subsequence.

LOGIC
-----
Naive Approach: The idea is to first sort the array and find the longest subarray with consecutive elements.
After sorting the array run a loop and keep a count and max (both initially zero). Run a loop from start to end and if the current element is not equal to the previous (element+1) then set the count to 1 else increase the count. Update max with a maximum of count and max.
Complexity Analysis:

Time complexity: O(nLogn).
Time to sort the array is O(nlogn).
Auxiliary space : O(1).
As no extra space is needed.


Efficient solution:
This problem can be solved in O(n) time using an Efficient Solution. The idea is to use Hashing. We first insert all elements in a Set. Then check all the possible starts of consecutive subsequences.

Algorithm:

Create an empty hash.
Insert all array elements to hash.
Do following for every element arr[i]
Check if this element is the starting point of a subsequence. To check this, simply look for arr[i] – 1 in the hash, if not found, then this is the first element a subsequence.
If this element is the first element, then count the number of elements in the consecutive starting with this element. Iterate from arr[i] + 1 till the last element that can be found.
If the count is more than the previous longest subsequence found, then update this.

Complexity Analysis:

Time complexity: O(n).
Only one traversal is needed and the time complexity is O(n) under the assumption that hash insert and search take O(1) time.
Auxiliary space : O(n).
To store every element in hashmap O(n) space is needed.

SOURCE
------
geeksforgeeks

CODE
----
'''

def lcs(l):
    freq = dict()
    for ele in l:
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1
         
    max_count = 1   
    for i in range(len(l)):
        if l[i] - 1 not in freq:
            ele = l[i]
            while ele in freq:
                ele += 1
            max_count = max(max_count, ele - l[i])
            
    return max_count
    
t = int(input())
for _ in range(t):
    size = int(input())
    l = [int(x) for x in input().split()]
    print(lcs(l))
