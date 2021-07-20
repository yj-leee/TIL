>시각

내가 쓴 풀이
```
n = int(input())

count = 0
h, m, s = 0, 0, 0

while h <= 5:
    for m in range(60):
        for s in range(60):
            s += 1
            if '3' in str(h) + str(m) + str(s):
                count += 1
    h += 1

print(count)
```

해설
```
h = int(input())

count = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1
print(count)

```
