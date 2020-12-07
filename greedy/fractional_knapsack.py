'''
PROBLEM STATEMENT
-----------------
Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item. 

 

Example 1:

Input:
N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}
Output: 240.00
Explanation: Total maximum value of item
we can have is 240.00 from the given
capacity of sack. 

Example 2:

Input:
N = 2, W = 50
values[] = {60,100}
weight[] = {10,20}
Output: 160.00
Explanation: Total maximum value of item
we can have is 160.00 from the given
capacity of sack.
 

Your Task :
Complete the function fractionalKnapsack() that receives maximum capacity , array of structure/class and size n and returns a double value representing the maximum value in knapsack.
Note: The details of structure/class is defined in the comments above the given function.

 

Constraints:
1 <= N <= 100
1 <= W <= 100

 

Expected Time Complexity : O(NlogN)
Expected Auxilliary Space: O(1)

LOGIC
-----
Sort the given items based on value/ weight and use greedy approach to maximize the final value

SOURCE
------
geeksforgeeks

CODE
-----
'''
def fractionalknapsack(W,Items,n):
    '''
    :param W: max weight which can be stored
    :param Items: List contianing Item class objects as defined in driver code, with value and weight
    :param n: size of Items
    :return: Float value of max possible value, two decimal place accuracy is expected by driver code
    
    {
        class Item:
        def __init__(self,val,w):
            self.value = val
            self.weight = w
    }
    '''
    # code here
    
    value_by_weight = list()
    total_value = 0
    
    value_by_weight = sorted(Items, key=lambda x: x.value/x.weight, reverse=True)
   
    for ele in value_by_weight:
        weight_val = ele.weight
        value_val = ele.value
        
        if W >= weight_val:
            W -= weight_val
            total_value += value_val
        else:
            fraction_value = W / weight_val
            total_value += (fraction_value * value_val)
            W -= int(fraction_value * weight_val)
            break
            
    return total_value
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]

        print("%.2f" %fractionalknapsack(W,Items,n))

# } Driver Code Ends
