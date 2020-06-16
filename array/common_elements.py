"""
PROBLEM STATEMENT
-----------------
Given three increasingly sorted arrays A, B, C of sizes N1, N2, and N3 respectively, you need to print all common elements in these arrays.

Note: Please avoid printing the same common element more than once.

Input:
First line contains a single integer T denoting the total number of test cases. T testcases follow. Each testcase contains four lines of input. First line consists of 3 integers N1, N2 and N3, denoting the sizes of arrays A, B, C respectively. The second line contains N1 elements of A array. The third lines contains N2 elements of B array. The fourth lines contains N3 elements of C array.

Output:
For each testcase, print the common elements of array. If not possible then print -1.

Constraints:
1 <= T <= 100
1 <= N1, N2, N3 <= 107
1 <= Ai, Bi, Ci <= 1018

Example:
Input:
1
6 5 8
1 5 10 20 40 80
6 7 20 80 100
3 4 15 20 30 70 80 120
Output:
20 80

Explanation:
Testcase1:  20 and 80 are the only common elements

LOGIC
-----

SOURCE
-----
geeksforgeeks

CODE
----
"""
#code
def common_element(ar1, ar2, ar3):
    i, j, k = 0, 0, 0
    count = 0
      
    # Iterate through three arrays while all arrays have elements     
    while (i < len(ar1) and j < len(ar2) and k< len(ar3)): 
          
        # If x = y and y = z, print any of them and move ahead  
        # in all arrays 
        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]): 
            print(ar1[i], end=" ") 
            count += 1
            i += 1
            j += 1
            k += 1
          
        # x < y     
        elif ar1[i] < ar2[j]: 
            i += 1
              
        # y < z     
        elif ar2[j] < ar3[k]: 
            j += 1
          
        # We reach here when x > y and z < y, i.e., z is smallest     
        else: 
            k += 1
            
    if count == 0:
        print("-1", end=" ")

t = int(input())
for _ in range(t):
    index = [int(x) for x in input().split()]
    l1 = [int(x) for x in input().split()]
    l2 = [int(x) for x in input().split()]
    l3 = [int(x) for x in input().split()]
    
    common_element(l1,l2,l3)
    print()
