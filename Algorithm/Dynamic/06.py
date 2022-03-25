n = int(input())
t = []
p = []
dp = [0] * (n + 1)
max_val = 0

for _ in range(n):
    time, price = map(int, input().split())
    t.append(time)
    p.append(price)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_val)
        max_val = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_val
