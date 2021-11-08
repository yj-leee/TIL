from collections import deque

n, l, r = map(int, input().split())

graph = []
datas = [[0 * n] * 3]

for _ in range(n):
    graph.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def process(x, y, number):
    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))

    union[x][y] = index
    summary = graph[x][y]
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx and nx < n and 0 <= ny and ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))  # 확인해야할 위치 저장

                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))

    for i, j in united:
        graph[i][j] = summary // count

    return count


total_count = 0
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == n * n:
        break
    total_count += 1

print(total_count)
