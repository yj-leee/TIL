# data = [[],[2,3,4],[4],[4]]
# visited = [false,false,false,false]
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


n, m, v = map(int, input().split())
graph = [] * n
visited = [False] * n

for i, j in range(m):
    graph[i].append(j)



dfs(graph, 1, visited)