'''
The task is to use depth-first search to compute the number of connected components in a given undirected graph.

Given: A simple graph with n≤103 vertices in the edge list format.
Return: The number of connected components in the graph.
'''

import networkx as nx

def my_dfs_function(visited, graph, node):

    if node not in visited:
      visited.add(node)
      #print(node, end= " ")

      for neighbour in dict(graph[node]).keys():
            my_dfs_function(visited, graph, neighbour)

with open('rosalind_cc.txt', 'r') as f:
    line = f.readline().split(" ")

    n = int(line[0])
    e = int(line[1])

    G = nx.read_edgelist(f, nodetype=int, create_using=nx.Graph)
    G.add_nodes_from(range(1,n+1))

    #nx.draw(G, with_labels=True, font_weight="bold")
    #plt.show()

#nx.number_connected_components(G)
#list(nx.dfs_edges(G))

visited = set()  # Set to keep track of visited nodes of graph.
nodes = set(G.nodes()) # Set to keep track of available nodes 
connected = 0

while len(nodes) > 0:
    
    my_dfs_function(visited, G, nodes.pop())
    connected = connected+1
    nodes = nodes-visited
    
print(connected)