from collections import deque


n, m, v = map(int, input().split())
visited = [False] * n
graph = [[0] * (n + 1) for _ in range(n + 1)]
print(graph)