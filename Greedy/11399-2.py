n= int(input())
data = list(map(int, input().split()))

data.sort()
minimum = 0
for i in range(n):
    for j in range(i + 1):
        minimum += data[j]
print(minimum)
