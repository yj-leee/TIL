>6094 : [기초-리스트] 이상한 출석 번호 부르기3(py) 해결


```
n = int(input())
k = input().split()

for i in range(n):
    k[i] = int(k[i])

t = k[1]
for i in range(n):
    if t > k[i]:
        t = k[i]
print(t)
```


모범 답안  
```
n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

min = a[0]
for i in range(0, n) :
  if a[i] < min :
    min = a[i]

print(min)


```
