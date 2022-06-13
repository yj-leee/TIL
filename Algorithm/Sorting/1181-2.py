n = int(input())
s = set()

for _ in range(n):
    s.add(input())

data = list(s)
data.sort()
data.sort(key=len)

for d in data:
    print(d)
