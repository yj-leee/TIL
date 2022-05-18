from collections import deque

n, m, v = map(int, input().split())
visited = [[False] for _ in range(n + 1)]
graph =[[] for _ in range(n + 1)]

for _ in range(n + 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
    

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    print(start, end=' ')
    
    for i in graph[start]:
        queue.popleft()
        if visited[i] == False:
            queue.append(i)
            bfs(graph, visited, i)
            
            
            
bfs(graph, visited, 1)

