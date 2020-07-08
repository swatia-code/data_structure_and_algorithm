'''
PROBLEM STATEMENT
-----------------
Given an array of integers where each element represents the max number of steps that can be made forward from that element. The task is to find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then cannot move through that element.

Input: 
The first line contains an integer T, depicting total number of test cases.  Then following T lines contains a number n denoting the size of the array. Next line contains the sequence of integers a1, a2, ..., an.

Output:
For each testcase, in a new line, print the minimum number of jumps. If answer is not possible print "-1"(without quotes).

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
0 <= ai <= 107

Example:
Input:
2
11
1 3 5 8 9 2 6 7 6 8 9
6
1 4 3 2 6 7
Output:
3
2

Explanation:
Testcase 1: First jump from 1st element, and we jump to 2nd element with value 3. Now, from here we jump to 5h element with value 9. and from here we will jump to last.
 
LOGIC
-----
maxReach The variable maxReach stores at all time the maximal reachable index in the array.
step The variable step stores the number of steps we can still take(and is initialized with value at index 0, i.e. initial number of steps)
jump jump stores the amount of jumps necessary to reach that maximal reachable position.
Given array arr = 1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9

maxReach = arr[0]; // arr[0] = 1, so the maximum index we can reach at the moment is 1.
step = arr[0]; // arr[0] = 1, the amount of steps we can still take is also 1.
jump = 1; // we will always need to take at least one jump.
Now, starting iteration from index 1, the above values are updated as follows:
First we test whether we have reached the end of the array, in that case we just need to return the jump variable.
if (i == arr.length - 1)
    return jump;
Next we update the maxReach. This is equal to the maximum of maxReach and i+arr[i](the number of steps we can take from the current position).
maxReach = Math.max(maxReach, i+arr[i]);
We used up a step to get to the current index, so steps has to be decreased.
step--;
If no more steps are remaining (i.e. steps=0, then we must have used a jump. Therefore increase jump. Since we know that it is possible somehow to reach maxReach, we again initialize the steps to the number of steps to reach maxReach from position i. But before re-initializing step, we also check whether a step is becoming zero or negative. In this case, It is not possible to reach further.
if (step == 0) {
    jump++;
    if(i>=maxReach)
       return -1;
    step = maxReach - i;
}

SOURCE
------
geeksforgeeks

CODE
----
'''
def minimum_number_of_jumps(l, n):
    
    if n <= 0:
        return 0
         
    #if the length of jumps from first element is zero, then there is no way to jump to resch the end
    if l[0] == 0:
        return -1
    #maximal reachable index in the array   
    max_reach = l[0]
    
    #amount of steps we can still take
    step = l[0]

    #amount of jumps necessary to reach that maximal reachable position 
    jump = 1
    
    for i in range(1, n):
        if i == n - 1:
            return jump
            
        max_reach = max(max_reach, i + l[i])
        
        step -= 1
        
        if step == 0:
            jump += 1
            
            if i >= max_reach:
                return -1
                
            step = max_reach - i
            
    return -1

t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    print(minimum_number_of_jumps(l, n))
