"""
PROBLEM STATEMENT
-----------------
Given a linked list L of N nodes, sorted in ascending order based on the absolute values of its data. Sort the linked list according to the actual values.
Ex: Input : 1 -> -2 -> -3 -> 4 -> -5 
      Output: -5 -> -3 -> -2 -> 1 -> 4

Input
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case contains a positive integer N denoting the size of linked list. The second line of each test case contains N space separated integers denoting the values of N nodes.


Output
Corresponding to each test case, the expected output will be space separated values of the sorted linked list.


Constraints
1 <= T <= 100
0 <   N  <= 30
-100 <= L[i] <= 100

Examples 

Input
2
3
1 -3 -4
4
0 -2 3 -10


Output
-4  -3  1
-10 -2  0  3

LOGIC
-----
An efficient solution can work in O(n) time. An important observation is, all negative elements are present in reverse order. So we traverse the list, whenever we find an element that is out of order, we move it to the front of linked list.

SOURCE
------
geeksforgeeks

CODE
----
"""
def sortList(head):
    '''
    head: head of linkedList
    
    Your method shouldn't print anything
    it should transform the passed linked list
    '''
    prev = head  
    curr = head.next
          
    while(curr != None):  
           
        if(curr.data < 0): 
                  
            prev.next = curr.next
            curr.next = head
            head = curr 
            curr = prev  
  
        else: 
            prev = curr 
  
        curr = curr.next
   
    return head
