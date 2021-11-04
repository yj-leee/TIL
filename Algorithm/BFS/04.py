n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int(input().split()))
# 최소값과 최대값 초기화
min_value = 1e9
max_value = -1e9


def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
        if mul > 0:
            dfs(i + 1, now * data[i])
        if div > 0:
            dfs(i + 1, int(now / data[i]))
            div += 1


# dfs 메서드 호출
dfs(1, data[0])

# 최댓값과 최소값 차례로 출력
print(max_value)
print(min_value)
