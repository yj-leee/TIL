from collections import deque

n, l, r = map(int, input().split())

graph = []
datas = [[0 * n] * 3]

for _ in range(n):
    graph.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def migration(x, y, number):
    population = 0
    count = 0

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.poplieft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if l <= graph[nx][ny] - graph[x][y] <= r:
                    population += graph[nx][ny]
                    count += 1
                    q.append((nx, ny))  # 확인해야할 위치 저장
                    datas[nx][ny] = number  # 방문 처리를 한다
        population = population // count

    return population


number = 1
x = 0
y = 0
while True:
    population = migration(x, y, number)

    for i in range(n):
        for j in range(n):
            if population == 0:
                break

            elif datas[i][j] == number:
                graph[i][j] = population
            number += 1


# print data 에서 가장 높은 수 ...?
