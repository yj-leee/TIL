from collections import deque

n, m, v = map(int, input().split())
visited = [False for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]


for _ in range(n + 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()



def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        q = queue.popleft()
        print(q, end=' ')
    
        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                



bfs(graph, visited, v)