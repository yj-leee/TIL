>큰 수의 법칙

내가 쓴 풀이
```
N,M,K = input().split()
d = list(map(int, input().split()))

n = int(N)
m = int(M)
k = int(K)

result = 0
count = 0
total_count = 0
temp = 0
while total_count <= m:
    if k != count:
        result += max(d)
        count += 1
        total_count += 1
        print(result)
    else:
        if total_count % k == 1:
            d.append(temp)
        else:
            temp = max(d)
            d.remove(temp)
        count = 0

print(result)
```

해설
```
case1
n, m, k = map(int, input().split())
data = list(map(int, input().split()))


# 정렬하기 -> 가장 큰 수, 두번째로 큰 수 구하기
data.sort()
first = data[n-1]
second = data[n-2]

result = 0
while True:
    for i in range(k):
        if m == 0:
            break;
        result += first
        m -= 1

    if m == 0:
        break;
    result += second
    m -= 1

print(result)


case2
n, m, k = map(int, input().split())
data = list(map(int, input().split()))


# 정렬하기 -> 가장 큰 수, 두번째로 큰 수 구하기
data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
# 가장 큰 수 더하기
result += (count) * first
# 두번째로 큰 수 더하기
result += (m - count) * second

print(result)
```
