def possible(answer):
    """
    x: 가로 좌표
    y: 세로 좌표
    stuff: 기둥 또는 보
    """
    for x, y, stuff in answer:
        # 설치된 것이 기둥인 경우
        if stuff == 0:
            # 바닥 위, 설치 지점에 보가 있는 경우, 설치 왼쪽 지점에 보가 있는 경우, 설치 아래 지점에 기둥이 있는 경우
            if (
                (y == 0)
                or ([x, y, 1] in answer)
                or [x - 1, y, 1] in answer
                or [x, y - 1, 0] in answer
            ):
                continue
            return False
        # 설치된 것이 보인 경우
        elif stuff == 1:
            # 한쪽 끝부분이 기둥 위,
            if (
                ([x, y - 1, 0] in answer)
                or ([x + 1, y, 0] in answer)
                or ([x - 1, y, 1] in answer)
            ):
                continue
            return False
        return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)
