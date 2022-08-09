import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False for _ in range(n + 1)]
graph = [[0]*m for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
def dfs(graph, visited, start):
    visited[start] = True
    global cnt
    cnt += 1
    for x in graph[start]:
        if visited[x] == False:
            dfs(graph, visited, start)



dfs(graph, visited, 1)
    