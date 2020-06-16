"""
PROBLEM STATEMENT
-----------------
Given an array having both positive and negative integers. The task is to complete the function maxLen() which returns the length of maximum subarray with 0 sum. The function takes two arguments an array A and n where n is the size of the array A.

Input:
The first line of input contains an element T denoting the number of test cases. Then T test cases follow. Each test case consists of 2 lines. The first line of each test case contains a number denoting the size of the array A. Then in the next line are space-separated values of the array A.

Output:
For each test case, the output will be the length of the largest subarray which has sum 0.

User Task:
Since this is a functional problem you don't have to worry about input, you just have to complete the function maxLen().

Expected Time Complexity: O(N*Log(N)).
Expected Space Complexity: O(N).

Constraints:
1 <= T <= 100
1 <= N <= 104
-1000 <= A[i] <= 1000, for each valid i

Example:
Input
1
8
15 -2 2 -8 1 7 10 23

Output
5

Explanation
Testcase 1: In the above test case the largest subarray with sum 0 will be -2 2 -8 1 7.

LOGIC
-----
Create a extra space, an array of length n (prefix), a variable (sum) , length (max_len) and a hash map (hm) to store sum-index pair as a key-value pair
Move along the input array from starting to the end
For every index update the value of sum = sum + array[i]
Check for every index, if the current sum is present in the hash map or not
If present update the value of max_len to maximum of difference of two indices (current index and index in the hash-map) and max_len
Else Put the value (sum) in the hash map, with the index as a key-value pair.
Print the maximum length (max_len)

SOURCE
------
geeksforgeeks

CODE
----
"""
#Your should return the required output
def maxLen1(n, arr):
    #Code here
    maxlen = 0
    for i in range(n):
        sum = arr[i]
        
        for j in range(i+1,n):
            sum += arr[j]
            if sum == 0:
                maxlen = max(maxlen,j-i+1)

    return maxlen

def maxLen(n, arr):
    maxlen = 0
    sum  = 0
    sum_index = dict()
    
    for i in range(n):
        sum += arr[i]
        
        if arr[i] == 0 and maxlen == 0:
            maxlen = 1
            
        if sum == 0:
            maxlen = i+1
            
        if sum in sum_index:
            maxlen = max(maxlen, i - sum_index[sum]) 
        else:
            sum_index[sum] = i

    return maxlen
    
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
