n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()
result = 0

while (k == 0):
    for i in coins:
        if i > k:
            pass
        else:
            if k % i == 0:
                result += (k // i)
                k -= (result * k)
print(result)
                
                    