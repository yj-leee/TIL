n = int(input())
k = int(input())
# 맵 정보
data = [[0] * (n + 1) for _ in range(n + 1)]

# 사과가 있는곳은 1로 표시
for _ in range(k):
    a, b = map(int, input().splint())
    data[a][b] = 1

# 방향 정보
info = []

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))


def turn(direction, c):
    """
    방향 회전 함수
    """
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


# 초기 뱀은 동쪽을 보고 있으므로, 동, 남, 서, 북 순서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def simulate():
    # 뱀의 머리 위치
    x, y = 1, 1
    # 뱀이 존재하는 위치는 2로 표시
    data[x][y] = 2
    # 처음 동쪽을 보고 있음
    direction = 0
    # 시작한 뒤에 지난 초
    time = 0
    # 다음에 회전할 정보
    index = 0
    # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    q = [(x, y)]

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # x 가 범위 안에 있는지 and y가 범위 안에 있는지 and 뱀의 몸통이 없는 위치인지
        if (1 <= nx and nx <= n) and (1 <= ny and ny <= n) and (data[nx][ny] != 2):
            # 사과가 있는지 확인, 사과가 없으면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append(nx, ny)
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있으면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽 또는 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        # 다음 위치로 머리를 이동
        x, y = nx, ny
        time += 1
        if index < l and time == info[index][0]:  # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
        return time
