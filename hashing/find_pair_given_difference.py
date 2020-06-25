'''
PROBLEM STATEMENT
-----------------
Given an unsorted array Arr[] and a number N. You need to write a program to find if there exists a pair of elements in the array whose difference is N.

Input:
First line of input contains an integer T which denotes the number of test cases. Then T test cases follows. First line of each test case contains two space separated integers L and N where L denotes the length of array or the number of elements in the array and N denotes the difference between two elements. Second line of each test case contains L space separated integers which denotes the elements of the array.

Output:
For each test case, in a new line print 1 if the pair is found otherwise print -1 if there does not exist any such pair.

Constraints:
1<=T<=100
1<=L<=104
1<=Arr[i]<=105

Example:
Input:
2
6 78
5 20 3 2 5 80
5 45
90 70 20 80 50
Output:
1
-1

LOGIC
-----

SOURCE
------
geeksforgeeks

CODE
----
'''
#code
def find_pair(l, k):
    freq = dict()
    for ele in l:
        if ele not in freq:
            if ele+k in freq or ele-k in freq:
                return True
            else:
                freq[ele] = 1
        
    return False

t = int(input())
for _ in range(t):
    l = [int(x) for x in input().split()]
    n = l[0]
    k = l[1]
    arr = [int(x) for x in input().split()]
    if find_pair(arr,k):
        print("1")
    else:
        print('-1')
