'''
PROBLEM STATEMENT
-----------------
Given an array of integers and a number k, write a function that returns true if given array can be divided into pairs such that sum of every pair is divisible by k.

Input:
The first line of input contains an integer T denoting the number of test cases. The T test cases follow. Each test case contains an integer n denoting the size of the array. The next line contains the n space separated integers forming the array. The last line contains the value of k.

Output:
Print "True" (without quotes) if given array can be divided into pairs such that sum of every pair is divisible by k or else "False" (without quotes).

Constraints:
1<=T<=100
2<=n<=10^5
1<=a[i]<=10^5
1<=k<=10^5

Example:
Input:
2
4
9 7 5 3
6
4
91 74 66 48
10

Output:
True
False

LOGIC
-----
1) If length of given array is odd, return false. 
    An odd length array cannot be divided into pairs.
2) Traverse input array and count occurrences of 
    all reminders. 
      freq[arr[i] % k]++
3) Traverse input array again. 
   a) Find the remainder of the current element.
   b) If remainder divides k into two halves, then
      there must be even occurrences of it as it 
      forms pair with itself only.
   c) If the remainder is 0, then there must be 
      even occurrences.
   c) Else, number of occurrences of current 
      the remainder must be equal to a number of 
      occurrences of "k - current remainder".
SOURCE
------
geeksforgeeks

CODE
----
'''
def isDivisible(l, k):
    #since we have to divide in pairs, length can't be odd
    if len(l)%2:
        return False
        
    #dict of frequency of remainder
    rem_freq = dict()
    for ele in l:
        if ele%k in rem_freq:
            rem_freq[ele%k] += 1
        else:
            rem_freq[ele%k] = 1
            
    for ele in l:
        rem = ele%k
        if rem == 0:
            if rem_freq[0]%2:
                return False
                
        elif 2*rem == k:
            if rem_freq[rem]%2:
                return False
                
        else:
            if (k -rem) in rem_freq :
                if rem_freq[rem] != rem_freq[k - rem]:
                    return False
            else:
                return False
                
    return True

t = int(input())
for _ in range(t):
    size = int(input())
    l = [int(x) for x in input().split()]
    k = int(input())
    print(isDivisible(l, k))
