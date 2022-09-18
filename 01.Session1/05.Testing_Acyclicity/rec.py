def tri_recursion(visited, k, space):
    blank = ""
    for i in range(0, space):
        blank = blank + "   "
    if(k > 0):
        
        print(blank + "k: " + str(k))
        result1 = k + tri_recursion(visited, k - 1, space+1)
        result2 = k - tri_recursion(visited, k - 1, space+1)
        print(blank + "result1: " + str(result1))
        print(blank + "result2: " + str(result2))

        visited.append(result1)
        visited.append(result2)
        print(blank, end= " ")
        print(visited)
    else:
        print(blank + "k: 0")
        result1 = 0
        result2 = 0
        print(blank + "result1: " + str(result1))
        print(blank + "result2: " + str(result2))
    return result1 + result2

print("\n\nRecursion Example Results")
visited = []
print(tri_recursion(visited, 2, 0))