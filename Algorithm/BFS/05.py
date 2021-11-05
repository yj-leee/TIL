from itertools import combinations, filterfalse

# 복도의  크기
n = int(input())
board = []

# 모든 선생님 위치 정보, 모든 빈 공간의 위치 정보
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님의 위치를 저장한다
        if board[i][j] == "T":
            teachers.append((i, j))
        # 모든 빈공간의 위치를 저장한다
        if board[i][j] == "X":
            spaces.append((i, j))

# 각각 선생님의 위치에서 상,하,좌,우 확인하여 학생이 감지되는지 확인하는 함수
def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            y -= 1
    # 오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            y += 1
    # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            x -= 1
    # 아래쪽 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            x += 1
    return False


# 장애물 설치 이후 한명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님의 위치를 하나씩 확인
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
        return False


find = False  # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 빈공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    # 장애물 설치해보기
    for x, y in data:
        board[x][y] = "O"
    # 학생이 한명도 감지되지 않는 경우
    if not process():
        find = True
        break
    # 설치된 장애물을 다시 없애기
    for x, y in data:
        board[x][y] = "X"

if find:
    print("YES")
else:
    print("NO")
