## Implements graph as adjacency list
from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
        stack.append(v)

    def topological_sort(self):
        #V = len(self.graph)
        #print(V)
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)

        print(stack[::-1])

        # The function to do Topological Sort.
    def kahn_sort(self):
        # Create a vector to store indegrees of all
        # vertices. Initialize all indegrees as 0.
        in_degree = [0] * (self.V)

        # Traverse adjacency lists to fill indegrees of
        # vertices.  This step takes O(V+E) time
        for i in self.graph:
           for j in self.graph[i]:
              in_degree[j] += 1

        # Create an queue and enqueue all vertices with
        # indegree 0
        queue = []
        for i in range(self.V):
           if in_degree[i] == 0:
              queue.append(i)

        # Initialize count of visited vertices
        cnt = 0

        # Create a vector to store result (A topological
        # ordering of the vertices)
        top_order = []

        # One by one dequeue vertices from queue and enqueue
        # adjacents if indegree of adjacent becomes 0
        while queue:
        # Extract front of queue (or perform dequeue)
        # and add it to topological order
           u = queue.pop(0)
           top_order.append(u)

           # Iterate through all neighbouring nodes
           # of dequeued node u and decrease their in-degree
           # by 1
           for i in self.graph[u]:
              in_degree[i] -= 1
              # If in-degree becomes zero, add it to queue
              if in_degree[i] == 0:
                 queue.append(i)

           cnt += 1

        # Check if there was a cycle
        if cnt != self.V:
           print ("There exists a cycle in the graph")
        else:
        # Print topological order
           print(top_order)


g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
print(g.graph)


#g.topological_sort()
g.kahn_sort(