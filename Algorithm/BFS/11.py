from collections import deque


def get_next_pos(pos, board):
    # 반환 결과(이동 가능한 위치들)
    next_pos = []

    # 현재 위치 정보
    pos = list(pos)
    pos1_x, pos1_y = pos[0][0], pos[0][1]
    pos2_x, pos2_y = pos[1][0], pos[1][1]

    # 상하좌우 이동하는 경우에 대해서 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y = pos1_x + dx[i], pos1_y + dy[i]
        pos2_next_x, pos2_next_y = pos2_x + dx[i], pos2_y + dy[i]

        # 이동(두칸)
        if (board[pos1_next_x][pos1_next_y]) == 0 and (
            board[pos2_next_x][pos2_next_y] == 0
        ):
            next_pos.append({(pos1_next_x, pos1_next_y), pos2_next_x, pos2_next_y})

    # 회전(현재 가로로 놓여있을 시 위 또는 아래)
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos2_x + i, pos2_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 회전(현재 세로로 놓여있을 시 왼쪽 또는 오른쪽)
    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y + i] and board[pos2_x][pos2_y + i]:
                next_pos.append({(pos1_x, pos1_y)(pos1_x, pos2_y + i)})
                next_pos.append({(pos2_x, pos2_y)(pos2_x, pos2_y + i)})

    return next_pos


def solution(board):
    # 맵의 외각에 벽을 두는 형태로 변형
    n = len(board)
    new_board = [[1] * (n + 1) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    # bfs
    q = deque()
    visited = []
    pos = {(1, 1), (2, 1)}
    q.append((pos, 0))
    visited.append(pos)

    while q:
        pos, cost = q.popleft()
        # (n, n) 위치에 도달했다면 최단거리이므로 반환
        if (n, n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0
