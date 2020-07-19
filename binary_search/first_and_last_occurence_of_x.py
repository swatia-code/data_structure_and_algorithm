'''
PROBLEM STATEMENT
-----------------
Given a sorted array with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.

Note: If the number x is not found in the array just print '-1'.

Input:
The first line consists of an integer T i.e number of test cases. The first line of each test case contains two integers n and x. The second line contains n spaced integers.

Output:
Print index of the first and last occurrences of the number x with a space in between.

Constraints: 
1<=T<=100
1<=n,a[i]<=1000

Example:
Input:
2
9 5
1 3 5 5 5 5 67 123 125
9 7
1 3 5 5 5 5 7 123 125

Output:
2 5
6 6

LOGIC
-----
An Efficient solution of this problem is to use binary search.
1. For the first occurrence of a number

  a) If (high >= low)
  b) Calculate  mid = low + (high - low)/2;
  c) If ((mid == 0 || x > arr[mid-1]) && arr[mid] == x)
         return mid;
  d) Else if (x > arr[mid])
        return first(arr, (mid + 1), high, x, n);
  e) Else
        return first(arr, low, (mid -1), x, n);
  f) Otherwise return -1; 
2. For the last occurrence of a number

  a) if (high >= low)
  b) calculate mid = low + (high - low)/2;
  c)if( ( mid == n-1 || x < arr[mid+1]) && arr[mid] == x )
         return mid;
  d) else if(x < arr[mid])
        return last(arr, low, (mid -1), x, n);
  e) else
       return last(arr, (mid + 1), high, x, n);      
  f) otherwise return -1; 

SOURCE
------
geeksforgeeks

CODE
----
'''
def binarySearch(arr,target,flag):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start+end)//2
        if (arr[mid] == target and flag) or arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start if flag else end
    
for _ in range(int(input())):
    n,target = map(int,input().split())
    arr = list(map(int,input().split()))
    leftIndex = binarySearch(arr,target,1)
    if leftIndex == len(arr) or arr[leftIndex] != target:
        print(-1)
    else:
        print(leftIndex,binarySearch(arr,target,0))
