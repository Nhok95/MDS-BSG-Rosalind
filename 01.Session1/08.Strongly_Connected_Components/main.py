'''
Given: A simple directed graph with n≤103 vertices in the edge list format.
Return: The number of strongly connected components in the graph.
'''

import networkx as nx
#import matplotlib.pyplot as plt

def splitLine2Int(line):
    a = int(line[0])
    b = int(line[1])
    return a,b

with open('rosalind_scc.txt', 'r') as f:
    line = f.readline().split(" ")

    n, e = splitLine2Int(line)

    G = nx.read_edgelist(f, nodetype=int, create_using=nx.DiGraph)
    G.add_nodes_from(range(1,n+1))

    #nx.draw(G, with_labels=True, font_weight="bold")
    #plt.show()

# Kosaraju's Algorithm

def first_dfs(visited, graph, node, stack):

    visited[node-1] = True

    for neighbour in dict(graph[node]).keys():
        if visited[neighbour-1] == False:
            first_dfs(visited, graph, neighbour, stack)
    
    stack.append(node)

def second_dfs(visited, graph, node):

    visited[node-1] = True

    for neighbour in dict(graph[node]).keys():
        if visited[neighbour-1] == False:
            second_dfs(visited, graph, neighbour)
    

stack = []
visited = [False]*n

for node in G.nodes():
    if visited[node-1] == False:
        first_dfs(visited, G, node, stack)

# Create the reverse graph
Gr = G.reverse()


# Mark all the vertices as not visited (For a second DFS)
visited = [False]*n

str_conn_components = 0

# Now process all vertices in order defined by Stack
while stack:
    node = stack.pop()
    if visited[node-1] == False:
        second_dfs(visited, Gr, node)
        str_conn_components = str_conn_components + 1

print(str_conn_components)

## Alternatively, we can do the first dfs over the reverse graph instead of the second one