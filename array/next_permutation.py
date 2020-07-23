'''
PROBLEM STATEMENT
-----------------
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers. If such arrangement is not possible, it must be rearranged as the lowest possible order ie, sorted in an ascending order.

For example:
1,2,3 → 1,3,2
3,2,1 → 1,2,3

Input:
The first line contains an integer T, depicting total number of test cases. Then following T lines contains an integer N depicting the size of array and next line followed by the value of array.

Output:
Print the array of next permutation in a separate line.

Constraints:
1 ≤ T ≤ 40
1 ≤ N ≤ 100
0 ≤ A[i] ≤ 100

Example:
Input:
1
6
1 2 3 6 5 4

Output:
1 2 4 3 5 6

LOGIC
-----
Following are few observations about the next greater number.
1) If all digits sorted in descending order, then output is always “Not Possible”. For example, 4321.
2) If all digits are sorted in ascending order, then we need to swap last two digits. For example, 1234.
3) For other cases, we need to process the number from rightmost side (why? because we need to find the smallest of all greater numbers)

You can now try developing an algorithm yourself.

Following is the algorithm for finding the next greater number.
I) Traverse the given number from rightmost digit, keep traversing till you find a digit which is smaller than the previously traversed digit. For example, if the input number is “534976”, we stop at 4 because 4 is smaller than next digit 9. If we do not find such a digit, then output is “Not Possible”.




II) Now search the right side of above found digit ‘d’ for the smallest digit greater than ‘d’. For “534976″, the right side of 4 contains “976”. The smallest digit greater than 4 is 6.

III) Swap the above found two digits, we get 536974 in above example.

IV) Now sort all digits from position next to ‘d’ to the end of number. The number that we get after sorting is the output. For above example, we sort digits in bold 536974. We get “536479” which is the next greater number for input 534976.

The above implementation can be optimized in following ways.
1) We can use binary search in step II instead of linear search.
2) In step IV, instead of doing simple sort, we can apply some clever technique to do it in linear time. Hint: We know that all digits are linearly sorted in reverse order except one digit which was swapped.

With above optimizations, we can say that the time complexity of this method is O(n).

SOURCE
------
geeksforgeeks

CODE
----
'''
def next_permutation(n, l):
    
    i = 0
    for i in range(n - 1, 0, -1):
        if l[i] > l[i - 1]:
            break
        
    if i == 1 and l[i] <= l[i - 1]:
        return sorted(l)
        
    smallest = i
    num = l[i - 1]
    for j in range(i , n):
        if l[j] > num and l[j] < l[smallest]:
            smallest = j
            
    l[smallest], l[i - 1] = l[i - 1], l[smallest]
    
    l_temp = sorted(l[i:])
    res = l[:i]
    for ele in l_temp:
        res.append(ele)
    
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    res = next_permutation(n, l)
    for ele in res:
        print(ele,end=" ")
    print()
