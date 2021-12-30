from collections import deque

# board 입력 받기
board = input()


# 목표 위치
target_x, target_y = 5, 5


count, x, y = 0, 1, 1
datas = []
datas.append([(count, x, y)])


# 로봇의 위치에서 벽이 감지되는지 확인
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for data in datas:
    q = deque(data)
    count, x, y = q.poplift()

    if x == target_x and y == target_y:
        print(count)
        break

    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]

        if 0 <= nx and nx < target_x and 0 <= ny and ny < target_y:
            if board[nx][ny] != 1:
                count += 1
                datas[count].append((nx, ny))
