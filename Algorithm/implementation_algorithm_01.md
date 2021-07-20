> 상하좌우 문제

```
n = int(input())
data = map(str, input().split())

x = 1
y = 1

for i in data:
    if i == 'R':
        y += 1
    elif i == 'U':
        x -= 1
    elif i == 'D':
        x += 1
    elif i == 'L':
        y -= 1

    if x == 0:
        x = 1
    elif y == 0:
        y = 1
    elif x == n+1:
        x = n
    elif y == n+1:
        y = n

print("{} {}".format(x, y))
```
```
n = int(input())
x, y = 1, 1
plans = input().split()


# L, R, U, D 에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동계획을 확인
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어나는 경우
            if nx < 1 or ny < 1 or nx > n or ny > n:
                continue
            # 이동 수행
            x, y = nx, ny
print(x, y)
```
