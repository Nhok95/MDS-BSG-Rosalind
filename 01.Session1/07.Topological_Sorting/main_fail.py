'''
Given: A simple directed acyclic graph with n≤103 vertices in the edge list format.
Return: A topological sorting (i.e., a permutation of vertices) of the graph.
'''

import networkx as nx
import matplotlib.pyplot as plt

def splitLine2Int(line):
    a = int(line[0])
    b = int(line[1])
    return a,b

with open('rosalind_ts.txt', 'r') as f:
    line = f.readline().split(" ")

    n, e = splitLine2Int(line)

    G = nx.read_edgelist(f, nodetype=int, create_using=nx.DiGraph)
    G.add_nodes_from(range(1,n+1))

    #nx.draw(G, with_labels=True, font_weight="bold")
    #plt.show()


def my_dfs_function(visited, graph, node, stack):

    if node not in visited:
      visited.add(node)
      stack.append(node)
      #print(node, end= " ")

      for neighbour in dict(graph[node]).keys():
            my_dfs_function(visited, graph, neighbour, stack)

visited = set()  # Set to keep track of visited nodes of graph.
nodes = set(G.nodes()) # Set to keep track of available nodes 
stack = []
sources = []

for node in G.nodes():
    if G.in_degree(node) == 0:
        sources.append(node) 

#print(sources)
if len(sources) > 0:
    my_dfs_function(visited, G, sources[0], stack)

else:
    print("No sources")

for i in range(0, len(stack)):
    if i != len(stack)-1:
        print(stack[i], end=" ")
    else:
        print(stack[i])  
    