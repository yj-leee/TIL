

내가 쓴 코드
```
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


a = sorted(a)
b = sorted(b, reverse=True)

count = 0
for i in range(n):
    if count != k:
        a[i] = b[i]
        count += 1
    else:
        print(sum(a))
        break
```

```
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
```
