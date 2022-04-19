from collections import deque


n, M, V = map(int, input().split())
visited = [False] * n
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(M):
  m1, m2 = map(int, input().split())
  # 노드 연결 하기
  graph[m1][m2] = graph[m2][m1] = 1

print(graph)

# BFS
def bfs(V):
    queue = deque([V])
    visited[V] = True
    
    while queue:
        v = queue.pop()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True



bfs(V)