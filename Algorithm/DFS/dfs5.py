from collections import deque


n, m, v = map(int, input().split())
graph = [] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
    
visited = [False * n]


def dfs(graph, v):
    queue = deque(graph[v])
    visited[v] = True
    while queue:
        queue.popleft()
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)


dfs(graph, v)