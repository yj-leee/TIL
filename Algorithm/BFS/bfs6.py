from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph.sort()
    graph.sort()


queue = deque(graph[v])
def bfs(graph, visited, start):
    while queue:
        visited[start] = True
        p = queue.popleft()
        print(p, end=' ')
        for i in graph[start]:
            if not visited[i]:
                bfs(graph, visited, start)
