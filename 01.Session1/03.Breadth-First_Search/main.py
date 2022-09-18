'''
The task is to use breadth-first search to compute single-source shortest distances in an unweighted directed graph.
Given: A simple directed graph with n≤103 vertices in the edge list format.
Return: An array D[1..n] where D[i] is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0). If i is not reachable from 1 set D[i] to −1.
'''

import networkx as nx

def my_bfs_function(graph, node, n):
    visited = []  # List to keep track of visited nodes.
    queue = []    # Initialize a queue
    shortest_distance = { i: -1 for i in range(0,n)}
    shortest_distance[0] = 0

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)

        for neighbour in dict(graph[s]).keys():
            if neighbour not in visited:
                shortest_distance[neighbour-1] = shortest_distance[s-1] +1
                visited.append(neighbour)
                queue.append(neighbour)

    for i in range(0,n):
      if i != n-1:
          print(shortest_distance[i], end=" ")
      else:
          print(shortest_distance[i])


with open('rosalind_bfs.txt', 'r') as f:
    line = f.readline().split(" ")

    n = int(line[0])
    e = int(line[1])

    G = nx.read_edgelist(f, nodetype=int, create_using=nx.DiGraph)
    G.add_nodes_from(range(len(G.nodes),n+1))


my_bfs_function(G, 1, n)