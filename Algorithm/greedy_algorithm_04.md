


```
n = int(input())
x = list(map(int, input().split()))

x.sort()
count = 0

for i in x:
    if n > 0:
        n = n - i
        count += 1
    else:
        print(count)
        break;
```


```
n = int(input())
data = list(map(int, input().split()))
data.sort()

# 총 그룹의 수
result = 0
# 현재 그룹에 포함된 모험가의 수
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
```

## 그리디 풀때 확인할 것

1. 문제를 풀기 위한 최소한의 아이디어를 떠올려라
2. 반드시 검토 해볼것!



