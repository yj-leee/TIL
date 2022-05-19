n, m, v = map(int, input().split())
graph = [[] for i in range(n + 1)]
visited = [False for i in range(n + 1)]

for _ in range(n+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()


def dfs(graph, visited, start):
    visited[start] = True
    print(start, end=" ")
    
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, start)


dfs(graph, visited, 1)

