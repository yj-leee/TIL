n = int(input())
data = []

for _ in range(n):
    i, j = map(int,input().split())
    data.append((i, j))

data.sort(key = lambda x: (x[1], x[0]))


cnt = 0
end = 0
for a, b in data:
    if a > end:
        cnt += 1
        end = b 

print(cnt)
