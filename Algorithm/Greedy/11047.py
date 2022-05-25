n, k = map(int, input().split())

result = 0
coins = []
for i in range(n):
    j = int(input())
    if k >= j:
        coins.append(j)
    
coins.sort(reverse=True)

for coin in coins:
    result += (k // coin)
    k %= coin
    if k == 0:
        print(result)
        break
    
