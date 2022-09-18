# 5. Testing Acyclicity
'''
Given: A positive integer k≤20 and k simple directed graphs in the edge list format with at most 103 vertices and 3⋅103 edges each.
Return: For each graph, output "1" if the graph is acyclic and "-1" otherwise.
'''

import networkx as nx

def splitLine2Int(line):
    a = int(line[0])
    b = int(line[1])
    return a,b

with open('rosalind_dag.txt', 'r') as f:
    k = int(f.readline())
    f.readline() # \n
    graphList = []
    for i in range(0,k):
        graphList.append(nx.DiGraph())

        line = f.readline().split(" ")
        n, e = splitLine2Int(line)

        graphList[i].add_nodes_from(range(1,n+1))

        for j in range(0,e):
            line = f.readline().split(" ")
            s, t = splitLine2Int(line)

            graphList[i].add_edge(s, t)
        
        f.readline() # \n

for i in range(0,k):
    G = graphList[i]

    try:
        cycles = list(nx.find_cycle(G, orientation="original"))
        print("-1", end= " ")
    except nx.exception.NetworkXNoCycle as e:
        print("1", end= " ")



