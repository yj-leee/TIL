>숫자 카드 게임

나의 풀이
```
n, m = map(int, input().split())

data = list()
for i in range(n):
    data.append(list(map(int, input().split())))

temp = min(data[0])
for i in range(n):
    if temp <= min(data[i]):
        temp = min(data[i])
print(temp)
```

해답
```
result = 0

for i in range(n):
    data = (list(map(int, input().split())))
    # 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수 들 중에서 가장 큰 수 찾기
    result = max(result, min_value) 

print(result)
```
