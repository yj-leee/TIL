>6093 : [기초-리스트] 이상한 출석 번호 부르기2(py)


```
# 출석 부른 횟수
n = int(input())

# 출석
k = input().split()

for i in range(n):
    k[i] = int(k[i])

# 거꾸로 출력
for i in range(n-1,-1,-1):
    print(k[i], end=' ')
```



모범 답안  
```
n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

for i in range(n-1, -1, -1):
  print(a[i], end=' ')

```
