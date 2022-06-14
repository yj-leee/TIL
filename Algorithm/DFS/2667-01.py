"""
깊이 우선 탐색
-스택 구조
-재귀 함수


"""

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))


count = 0
result = 0


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
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
        if dfs(i, j) == True:
            data.append(count)
            result += 1
            count = 0
            
data.sort()
print(result)

for i in range(len(data)):
    print(data[i])
            
    
    