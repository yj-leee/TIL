n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

print(graph)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

data = []
for i in range(n):
    for j in range(n):
        count = 0
        if dfs(i, j):
            data.append(count)

data.sort()

print(len(data))
for d in data:
    print(d)

