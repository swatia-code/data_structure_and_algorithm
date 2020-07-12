'''
PROBLEM STATEMENT
-----------------
Given a matrix of dimension r*c where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

So, we have to determine what is the minimum time required to rot all oranges. A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. If it is impossible to rot every orange then simply return -1.

Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains two integers r and c, where r is the number of rows and c is the number of columns in the array a[]. Next line contains space separated r*c elements each in the array a[].

Output:
Print an integer which denotes the minimum time taken to rot all the oranges (-1 if it is impossible).

Constraints:
1 <= T <= 100
1 <= r <= 100
1 <= c <= 100
0 <= a[i] <= 2

Example:
Input:
2
3 5
2 1 0 2 1 1 0 1 2 1 1 0 0 2 1
3 5
2 1 0 2 1 0 0 1 2 1 1 0 0 2 1

Output:
2
-1

Explanation:
Testcase 1:
2 | 1 | 0 | 2 | 1
1 | 0 | 1 | 2 | 1
1 | 0 | 0 | 2 | 1

Oranges at positions {0,0}, {0, 3}, {1, 3} and {2, 3} will rot oranges at {0, 1}, {1, 0}, {0, 4}, {1, 2}, {1, 4}, {2, 4} during 1st unit time. And, during 2nd unit time, orange at {1, 0} got rotten and will rot orange at {2, 0}. Hence, total 2 unit of time is required to rot all oranges.
 
LOGIC
-----
The idea is to use Breadth First Search. The condition of oranges getting rotten is when they come in contact with other rotten oranges. This is similar to breadth-first search where the graph is divided into layers or circles and the search is done from lower or closer layers to deeper or higher layers. In the previous approach, the idea was based on BFS but the implementation was poor and inefficient. To find the elements whose values are no the whole matrix had to be traversed. So that time can be reduced by using this efficient approach of BFS.
Algorithm:
Create an empty queue Q.
Find all rotten oranges and enqueue them to Q. Also enqueue a delimiter to indicate the beginning of next time frame.
Run a loop While Q is not empty
Do following while delimiter in Q is not reached
Dequeue an orange from the queue, rot all adjacent oranges. While rotting the adjacent, make sure that the time frame is incremented only once. And the time frame is not incremented if there are no adjacent oranges.
Dequeue the old delimiter and enqueue a new delimiter. The oranges rotten in the previous time frame lie between the two delimiters.

SOURCE
------
geeksforgeeks

CODE
----
'''
def one_find(a, n, m):
    for i in range(n):
        for j in range(m):
           if a[i][j]==1:
                return 1
    return 0

def delimeter(p):
    return (p[0]==-1 or p[1]==-1)

def bfs(a,n,m):
    q=[]
    ans=0
    
    for i in range(n):
        for j in range(m):
            if a[i][j]==2:
                q.append([i,j])
    
    q.append([-1,-1])
    
    while q!=[]:
        flag=0
        
        while delimeter(q[0])!=1:
            
            temp=q.pop(0)
            
            x=temp[0]
            y=temp[1]
            
            if x-1>=0 and a[x-1][y]==1:
                if flag==0:
                    ans+=1
                    flag=1
                a[x-1][y]=2
                q.append([x-1,y])
            
            if x+1<n and a[x+1][y]==1:
                if flag==0:
                    ans+=1
                    flag=1
                a[x+1][y]=2
                q.append([x+1,y])
            
            if y-1>=0 and a[x][y-1]==1:
                if flag==0:
                    ans+=1
                    flag=1
                a[x][y-1]=2
                q.append([x,y-1])
            
            if y+1<m and a[x][y+1]==1:
                if flag==0:
                    ans+=1
                    flag=1
                a[x][y+1]=2
                q.append([x,y+1])
        
        q.pop(0)
        if q!=[]:
            q.append([-1,-1])
  
    if one_find(a,n,m):
        print(-1)
    else:
        print(ans)

for _ in range(int(input())):
    n,m=map(int,input().split())
    temp=list(map(int,input().split()))
    a=[]
    k=0
    for i in range(n):
        a.append(temp[k:k+m])
        k+=m
    bfs(a,n,m)
    
    
    
