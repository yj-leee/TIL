n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

print(n)
print(graph)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0

def dfs(x, y):
    for i in range(4):
        x += dx[i]
        y += dy[i]
        if graph[x][y] == 1:
            dfs(x, y)
            global count
            graph[x][y] = 0
        else:
            return


result = []
for i in range(n):
    for j in range(n):
        result.append(dfs(i, j))

result.sort()
print(len(result))
for r in result:
    print(r)
