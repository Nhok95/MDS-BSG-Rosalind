# 6. Square in a Graph
'''
Given: A positive integer k≤20 and k simple undirected graphs with n≤400 vertices in the edge list format.
Return: For each graph, output "1" if it contains a simple cycle (that is, a cycle which doesn’t intersect itself) of length 4 and "-1" otherwise.
'''

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def splitLine2Int(line):
    a = int(line[0])
    b = int(line[1])
    return a,b

with open('ex6.txt', 'r') as f:
    k = int(f.readline())
    f.readline() # \n

    graphList = []
    for i in range(0,k):
        graphList.append(nx.Graph())

        line = f.readline().split(" ")
        n, e = splitLine2Int(line)
        #print("read" + " " + str(n) + " " + str(e))
        graphList[i].add_nodes_from(range(1,n+1))

        for j in range(0,e):
            line = f.readline().split(" ")
            s, t = splitLine2Int(line)

            #print( str(s) + " " + str(t))
            graphList[i].add_edge(s, t)
        
        f.readline() # \n

    nx.draw(graphList[2], with_labels=True, font_weight="bold")
    plt.show()

G = graphList[2]
n = len(G.nodes())

diagonal = [y for (_,y) in list(G.degree(G.nodes))]
diag_matrix = np.diagflat(diagonal)
matrix = (nx.adjacency_matrix(G)).todense()
laplacian = diag_matrix-matrix

print(diag_matrix)
print(matrix)
print(laplacian)


trace = np.trace(laplacian)
rank = np.linalg.matrix_rank(laplacian)

print(trace)
print(rank)
print(trace- 2*rank)