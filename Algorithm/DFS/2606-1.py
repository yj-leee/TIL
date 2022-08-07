n = int(input())
connect = int(input())
visited = [False for _ in range(n + 1)]
data = [[] for _ in range(n + 1)] 

for _ in range(connect):
    i, j = map(int, input().split())
    data[i].append(j)
    data[j].append(i)

cnt = 0
def dfs(start, graph, visited):
    visited[start] = True
    global cnt
    for i in graph[start]:
        if visited[i] == False:
            cnt += 1
            dfs(i, graph, visited)

dfs(1, data, visited)
print(cnt)
