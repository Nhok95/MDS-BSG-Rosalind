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

#list(nx.find_cycle(G, orientation="original"))

def my_dfs(visited, stack, graph, node):

    visited.add(node)
    stack[node-1] = True

    #print(dict(graph[node]).keys())
    for neighbour in dict(graph[node]).keys():
        if neighbour not in visited:
            if my_dfs(visited, stack, graph, neighbour) == True:
                return True
        elif recStack[neighbour-1] == True:
            return True

    stack[node-1] = False
    return False


for i in range(0,k):

    G = graphList[i]

    nodes = set(G.nodes())
    visited = set()

    nodes = nodes-visited

    while len(nodes) > 0:
        #print(visited)
        #print(nodes)
        node = nodes.pop()
        #print(node)

        recStack = [False] * (len(G.nodes()))
        
        result = 1
        if my_dfs(visited, recStack, G, node) == True:
            result = -1
            break;

    if i != k-1:
        print(str(result), end=" ")
    else:
        print(str(result))



