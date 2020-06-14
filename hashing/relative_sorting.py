"""
PROBLEM STATEMENT
-----------------
Given two arrays A1[] and A2[] of size N and M respectively. The task is to sort A1 in such a way that the relative order among the elements will be same as those in A2. For the elements not present in A2, append them at last in sorted order. It is also given that the number of elements in A2[] are smaller than or equal to number of elements in A1[] and A2[] has all distinct elements.
Note: Expected time complexity is O(N log(N)).

Input:
First line of input contains number of testcases. For each testcase, first line of input contains length of arrays N and M and next two line contains N and M elements respectively.

Output:
Print the relatively sorted array.

Constraints:
1 ≤ T ≤ 100
1 ≤ N,M  ≤ 106
1 ≤ A1[], A2[] <= 106

Example:
Input:
2
11 4
2 1 2 5 7 1 9 3 6 8 8
2 1 8 3
8 4
2 6 7 5 2 6 8 4 
2 6 4 5
Output:
2 2 1 1 8 8 3 5 6 7 9
2 2 6 6 4 5 7 8

Explanation:
Testcase 1: After sorting the resulted output is 2 2 1 1 8 8 3 5 6 7 9.
Testcase 2: After sorting the resulted output is 2 2 6 6 4 5 7 8.

LOGIC
-----
1. store all the elements in dictionary along with their frequency of occurance  in the first list
2. Iterate through the second dictionary and store element if in dictionary(and delete this entry) in a separate list.
3. If the dictionary is still not exhausted, sort it according to keys and store them in the new list

SOURCE
-----
geeksforgeeks

CODE
----
"""

#code
def relative_sorting(n, m, l1, l2):
    order = dict()
    
    for ele in l1:
        if ele not in order:
            order[ele] = 1
        else:
            order[ele] += 1
            
    res = list()
    
    for ele in l2:
        if ele in order:
            for i in range(order[ele]):
                res.append(ele)
            order.pop(ele)
            
    if len(order):
        for ele in sorted(order):
            for i in range(order[ele]):
                res.append(ele)
            
    for ele in res:
        print(ele, end=' ')
        
    print()

t = int(input())
for _ in range(t):
    sizes = [int(x) for x in input().split()]
    l1 = [int(x) for x in input().split()]
    l2 = [int(x) for x in input().split()]
    relative_sorting(sizes[0],sizes[1],l1,l2)
