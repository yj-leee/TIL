import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
def dfs(v):
    visited[v] = True
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv)

for v in range(1, n + 1):
    if not visited[v]:
        dfs(v)
        cnt += 1

print(cnt)
