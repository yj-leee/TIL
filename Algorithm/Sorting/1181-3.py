n = int(input())
data = set()

for _ in range(n):
    data.add(input())

words = []
for d in data:
    words.append(d)


words.sort(key= lambda x: (len(x), x))

for w in words:
    print(w)
