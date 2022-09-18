'''
Given: A simple directed acyclic graph with n≤103 vertices in the edge list format.
Return: A topological sorting (i.e., a permutation of vertices) of the graph.
'''

import networkx as nx
#import matplotlib.pyplot as plt

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


def topologicalSort(visited, graph, node, stack):
    visited[node-1] = True

    for neighbour in dict(graph[node]).keys():
        if visited[neighbour-1] == False:
            topologicalSort(visited, graph, neighbour, stack)

    stack.insert(0,node) #Push

visited = [False]*n
stack = []

for node in G.nodes():
    if visited[node-1] == False:
        topologicalSort(visited, G, node, stack)

for i in range(0, len(stack)):
    if i != len(stack)-1:
        print(stack[i], end=" ")
    else:
        print(stack[i])
    