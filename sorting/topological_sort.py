"""
LOGIC
-----

Topological sorting for Directed Acyclic Graph(DAG) is a linerar ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering.Topological Sorting is not possible if the graph is not DAG. There can be more than one topological sorting for a graph. The first vertex in topological sorting is always a vertex with in-degree as 0(a vertex with no incoming edges).

In DFS, we start from a vertex, we print it and then recursively call DFS for it's adjacent vertices. In, topological sorting, we use a temporary stack.We don't print the vertx immediately, we first recursively call topological sortingfor all it's adjacent vertices, then push it to a stack. Finally, print contents of stack. Note that a vertex is pushed too stack only when all of it's adjacent vertices(and their adjacent vertices and so on) are already in stack.

CODE
----
"""

def topologicalSort(i,visited,stack,graph):
    visited[i] = True
    
    for v in graph[i]:
        if visited[v]== False:
            topologicalSort(v,visited,stack,graph)
            
    stack.insert(0,i)

def topoSort(n, graph):
    # Code here
    visited = dict()
    for i in range(n):
        visited[i] = False
        
    stack = list()
        
    for i in range(n):
        if visited[i]== False:
            topologicalSort(i,visited,stack,graph)
            
    return stack


