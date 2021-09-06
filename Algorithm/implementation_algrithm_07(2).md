
```
lock = [[1,1,1],[1,1,0],[1,0,1]]
key = [[0,0,0],[1,0,0],[0,1,1]]

start = len(key) - 1 #2
end = start + len(lock) #4
expendSize = len(lock) + start * 2 #7
expendList = [[0] * expendSize for _ in range(expendSize)] # 배열 생성


def soultion():
    for a in range(0, 4): # 회전 방향
        for i in range(end): # 오른쪽으로 움직이기
            for j in range(end): # 아래로 움직이기
                if check(i, j, key, lock, start, end):
                    return True
        key = rotation(key)
    return False

def check(startX, startY, key, lock, start, end):    
    # expendList에 key 추가
    for i in range(len(key)):
        for j in range(len(key)):
            expendList[startX + i][startY + j] += key[i][j]

    # expendList에 lock 추가하면서 기존 값이랑 더하기
    for i in range(start, end):
        for j in range(start, end):
            expendList[i][j] += lock[i - start][j - start]
            if expendList[i][j] != 1:
                return False

def rotation(arr):
    n = len(arr)
    ret = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = arr[i][j]
    return ret
```