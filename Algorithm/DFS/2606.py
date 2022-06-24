n = int(input())
connect = int(input())


graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(connect):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


cnt = 0
def dfs(start, visited, graph):
    visited[start] = True
    global cnt 

    for i in graph[start]:
        if visited[i] == False:
            dfs(i, visited, graph)
            cnt += 1    


dfs(1, visited, graph)
print(cnt)
