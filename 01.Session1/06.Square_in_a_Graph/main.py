# 6. Square in a Graph
'''
Given: A positive integer k≤20 and k simple undirected graphs with n≤400 vertices in the edge list format.
Return: For each graph, output "1" if it contains a simple cycle (that is, a cycle which doesn’t intersect itself) of length 4 and "-1" otherwise.
'''

import networkx as nx
import numpy as np
from numpy.linalg import matrix_power
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


def splitLine2Int(line):
    a = int(line[0])
    b = int(line[1])
    return a,b

with open('rosalind_sq.txt', 'r') as f:
    k = int(f.readline())
    f.readline() # \n

    graphList = []
    for i in range(0,k):
        graphList.append(nx.Graph())

        line = f.readline().split(" ")
        n, e = splitLine2Int(line)
        graphList[i].add_nodes_from(range(1,n+1))

        for j in range(0,e):
            line = f.readline().split(" ")
            s, t = splitLine2Int(line)

            graphList[i].add_edge(s, t)
        
        f.readline() # \n


def find_square_cycles(adj_matrix_2):

    n = adj_matrix_2.shape[0]
    for i in range(0,n):
        for j in range(0,n):
            if (i==j):
                continue # skip this pair
            if (matrix_2[i,j] > 1):
                return 1     # Cycle found
    return -1 # No cycle length 4'''


for i in range(0,k):
    G = graphList[i]

    matrix = (nx.adjacency_matrix(G)).todense()
    matrix_2 = matrix_power(matrix,2)

    result = find_square_cycles(matrix_2)

    if i != k-1:
        print(str(result), end=" ")
    else:
        print(str(result))