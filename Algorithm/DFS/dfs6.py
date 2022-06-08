n, m, v = map(int, input().split())
visited = [False for i in range(n + 1)]
graph = [[] for i in range( n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort
    graph[b].sort
    
    
def dfs(graph, visited, start):
    visited[graph[start][0]] = True
    print(graph[start][0], end=" ")
    for i in graph[start][1:]:
        if not visited[i]:
            dfs(graph, visited, start)
            


    
    