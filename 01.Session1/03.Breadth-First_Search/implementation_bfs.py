'''
The task is to use breadth-first search to compute single-source shortest distances in an unweighted directed graph.
Given: A simple directed graph with n≤103 vertices in the edge list format.
Return: An array D[1..n] where D[i] is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0). If i is not reachable from 1 set D[i] to −1.
'''

import networkx as nx

with open('ex3.txt', 'r') as f:
    line = f.readline().split(" ")

    n = int(line[0])
    e = int(line[1])

    G = nx.read_edgelist(f, nodetype=int, create_using=nx.DiGraph)
    G.add_nodes_from(range(len(G.nodes),n+1))


d = 1
shortest_distance = [-1]*n
shortest_distance[0] = 0
for nodes in dict(nx.bfs_successors(G,1)).values():
    for node in nodes:
      shortest_distance[node-1] = d
    d = d+1

for i in range(0,n):
    if i != n:
        print(shortest_distance[i], end=" ")
    else:
        print(shortest_distance[i])