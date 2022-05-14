from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().slit())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()
    
    

def bfs(graph, start, visited):
    queue = deque(graph[start])    
    while queue:
        visited[start] = True
        print(start, " ")
        queue.poplift()
        for i in range(graph[start]):
            if not visited:
                queue.append(i)
                
                
bfs(graph, start, visited)
            
    

    
    