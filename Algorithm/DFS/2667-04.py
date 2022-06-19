from itertools import count


n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

print(graph)


count = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        global count
        count += 1
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            dfs(a, b)
        return True
    return False

result = []

for i in range(n):
    for j in range(n):
        count = 0
        if dfs(i, j):
            result.append(count)

result.sort()
print(len(result))
for r in result:
    print(r)
