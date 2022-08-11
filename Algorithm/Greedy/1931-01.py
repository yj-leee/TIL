n = int(input())
data = []

for _ in range(n):
    i, j = map(int, input().split())
    data.append((i, j))


data.sort(key=lambda x: (x[1], x[0]))
end = 0
count = 0
for i, j in data:
    if i > end:
        count += 1
        end = j

print(count)
