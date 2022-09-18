'''
An undirected graph is connected if there is a path connecting any two nodes. 
A tree is a connected (undirected) graph containing no cycles; this definition 
forces the tree to have a branching structure organized around a central core 
of nodes, just like its living counterpart.
We have already grown familiar with trees in “Mendel's First Law”, where we 
introduced the probability tree diagram to visualize the outcomes of a 
random variable.

In the creation of a phylogeny, taxa are encoded by the tree's leaves, or nodes 
having degree 1. A node of a tree having degree larger than 1 is called an 
internal node.

Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph 
on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree.
'''

import networkx as nx
import matplotlib.pyplot as plt


with open('rosalind_tree.txt', 'r') as f:
    n = int(f.readline())

    G = nx.read_edgelist(f, nodetype=int, create_using=nx.Graph)
    G.add_nodes_from(range(1,n+1))

    #nx.draw(G, with_labels=True, font_weight="bold")
    #plt.show()

def my_dfs_function(visited, graph, node):

    if node not in visited:
      visited.add(node)

      for neighbour in dict(graph[node]).keys():
            my_dfs_function(visited, graph, neighbour)

# Find the connected components of the graph
visited = set()  # Set to keep track of visited nodes of graph.
nodes = set(G.nodes()) # Set to keep track of available nodes 
connected = 0

while len(nodes) > 0:
    
    my_dfs_function(visited, G, nodes.pop())
    connected = connected+1
    nodes = nodes-visited

# Solution: Return the count of the component minus 1
print(connected-1)