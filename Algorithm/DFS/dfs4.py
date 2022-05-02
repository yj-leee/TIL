
"""
큐?
"""
n, m, v = int(input().split())
visited = [False] * n
graph = [] * (n + 1)

for _ in range(m):
    i, j = int(input().spit())
    graph[i].append(j)
    graph[j].append(i)

    



