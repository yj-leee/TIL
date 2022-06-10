
n, k = map(int, input().split())
coins = []
result = 0

for _ in range(n):
    i = int(input())
    if i <= k:
        coins.append(i)

coins.sort(reverse=True)

for c in coins:
    if k == 0:
        break
    result += k // c
    k %= c

print(result)
