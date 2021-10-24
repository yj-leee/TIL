from collections import deque


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

    # 모든 도시에 대한 최단거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()

    for next_node in graph[now]:
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
