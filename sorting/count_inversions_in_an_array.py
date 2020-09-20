'''
PROBLEM STATEMENT
-----------------
Given an array of positive integers. The task is to find inversion count of array.

Inversion Count : For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, the size of array. The second line of each test case contains N elements.

Output:
Print the inversion count of array.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
1 ≤ C ≤ 1018

Example:
Input:
1
5
2 4 1 3 5

Output:
3

Explanation:
Testcase 1: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

LOGIC
-----
Suppose the number of inversions in the left half and right half of the array (let be inv1 and inv2), what kinds of inversions are not accounted for in Inv1 + Inv2? The answer is – the inversions that need to be counted during the merge step. Therefore, to get a number of inversions, that needs to be added a number of inversions in the left subarray, right subarray and merge().
How to get number of inversions in merge()?
In merge process, let i is used for indexing left sub-array and j for right sub-array. At any step in merge(), if a[i] is greater than a[j], then there are (mid – i) inversions. because left and right subarrays are sorted, so all the remaining elements in left-subarray (a[i+1], a[i+2] … a[mid]) will be greater than a[j]

Algorithm:
The idea is similar to merge sort, divide the array into two equal or almost equal halves in each step until the base case is reached.
Create a function merge that counts the number of inversions when two halves of the array are merged, create two indices i and j, i is the index for first half and j is an index of the second half. if a[i] is greater than a[j], then there are (mid – i) inversions. because left and right subarrays are sorted, so all the remaining elements in left-subarray (a[i+1], a[i+2] … a[mid]) will be greater than a[j].
Create a recursive function to divide the array into halves and find the answer by summing the number of inversions is the first half, number of inversion in the second half and the number of inversions by merging the two.
The base case of recursion is when there is only one element in the given half.
Print the answer

SOURCE
------
GEEKSFORGEEKS

CODE
----
'''
def merge(start, mid, end, l, temp):
    
    inv = 0
    i = start 
    j = mid + 1
    k = start
    
    while(i<= mid  and j <= end):
        if l[i] <= l[j]:
            temp[k] = l[i]
            i += 1
            k += 1
        else:
            temp[k] = l[j]
            j += 1
            k += 1
            inv += (mid - i + 1)
            
    while(i <= mid ):
        temp[k] = l[i]
        k += 1
        i += 1
        
    while(j <= end):
        temp[k] = l[j]
        j += 1
        k += 1
        
    for i in range(start, end + 1):
        l[i] = temp[i]
        
    return inv

def merge_sort_helper(start, end, l, temp):
    
    inv = 0
    
    if start < end:
        
        mid = (end + start)//2
        
        inv += merge_sort_helper(start, mid, l, temp)
        inv += merge_sort_helper(mid + 1, end, l, temp)
        inv += merge(start, mid, end, l, temp)
        
    return inv
        
def merge_sort(l,n):
    start = 0
    end = n - 1
    temp = [0] * n
    return merge_sort_helper(start, end, l, temp)

t = int(input())
for i in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    print(merge_sort(l,n))
