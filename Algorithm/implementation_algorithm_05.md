
```
n = input()
length = len(n)
summary = 0

# 왼쪽 부분의 자리수 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자리수 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])


if summary == 0:
    print("LUCKY")
else:
    print("READY")

```

