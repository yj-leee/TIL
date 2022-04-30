N = int(input())
array = list(map(int, input().split()))

array.sort()
t = 0
for i in range(N):
    for j in range(i-1):
        print(i, j)
        if j < 0:
            pass
        t += array[i] + array[j]

print(t)
