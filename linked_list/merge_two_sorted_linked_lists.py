'''
PROBLEM STATEMENT
-----------------

Given two sorted linked lists consisting of N and M nodes respectively. The task is to merge both of the list (in-place) and return head of the merged list.
Note: It is strongly recommended to do merging in-place using O(1) extra space.

Example 1:

Input:
N = 4, M = 3 
valueN[] = {5,10,15,40}
valueM[] = {2,3,20}
Output: 2 3 5 10 15 20 40
Explanation: After merging the two linked
lists, we have merged list as 2, 3, 5,]
10, 15, 20, 40.
Example 2:

Input:
N = 2, M = 2
valueN[] = {1,1}
valueM[] = {2,4}
Output:1 1 2 4
Explanation: After merging the given two
linked list , we have 1, 1, 2, 4 as
output.
Your Task:
The task is to complete the function sortedMerge() which takes references to the heads of two linked lists as the arguments and returns the head of merged linked list.

Expected Time Complexity : O(n+m)
Expected Auxilliary Space : O(1)

Constraints:
1 <= N, M <= 104
1 <= Node's data <= 105

LOGIC
-----
Compare the head of both linked lists.
Find the smaller node among the two head nodes. The current element will be the smaller node among two head nodes.
The rest elements of both lists will appear after that.
Now run a recursive function with parameters, the next node of the smaller element and the other head.
The recursive function will return the next smaller element linked with rest of the sorted element. Now point the next of current element to that, i.e curr_ele->next=recursivefunction()
Handle some corner cases.
If both the heads are NULL return null.
If one head is null return the other.

SOURCE
------
geeksforgeeks

CODE
----
'''
import sys
sys.setrecursionlimit(100000)
def sortedMerge(head_A, head_B):
    if head_A is None and head_B is None:
        return None
        
    if head_A is None:
        return head_B
        
    if head_B is None:
        return head_A
        
    if head_A.data < head_B.data:
        head_A.next = sortedMerge(head_A.next, head_B)
        return head_A
        
    else:
        head_B.next = sortedMerge(head_A, head_B.next)
        return head_B
