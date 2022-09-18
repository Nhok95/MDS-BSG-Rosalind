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
        #print(n)
        #print(e)

        graphList[i].add_nodes_from(range(1,n+1))

        for j in range(0,e):
            line = f.readline().split(" ")
            s, t = splitLine2Int(line)

            graphList[i].add_edge(s, t)
        
        f.readline() # \n

G = graphList[18]

def rec(visited, stack, graph, node, space):

    blank = ""
    for i in range(0, space):
        blank = blank + "   "

    print(blank + "node: " + str(node))

    visited.add(node)
    stack[node-1] = True

    print(blank, end="")
    print(visited)
    print(blank, end="")
    print(stack)
    print(blank, end="")
    print(dict(graph[node]).keys())
    for neighbour in dict(graph[node]).keys():
        print(blank + "neigh: " + str(neighbour))
        if neighbour not in visited:
            print(blank + "neighbour: " + str(neighbour))
            if rec(visited, stack, graph, neighbour, space+1) == True:
                print(blank + "--1")
                return True # Cycle (recur)
        elif recStack[neighbour-1] == True:
            print(blank + "--2")
            return True # Cycle (found)

    print(blank + "--3")
    stack[node-1] = False
    return False # No Cycle

    #else:
    #    print(blank + "node [" + str(node) + "] visited!!")


visited = set()
recStack = [False] * (n)
print(rec(visited, recStack, G, 1, 0))
print(visited)

'''
7 7
1 2
2 3
2 4
4 3
1 5
5 6
5 7'''