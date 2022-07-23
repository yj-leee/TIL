n, k = map(int, input().split())

coins = []

for _ in range(n):
    c = int(input())
    if c < k:
        coins.append(c)


coins.sort(reverse=True)

result = 0
for coin in coins:
    if k == 0:
        print(result)
        break;
    result += k // coin
    k %= coin
