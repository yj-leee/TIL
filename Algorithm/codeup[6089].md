

>6089 : [기초-종합] 수 나열하기2(py)

```
a,r,n = input().split()

a = int(a)
r = int(r)
n = int(n)


for i in range(2, n+1):
    if i == 2:
        g = a * r
    else:
        g *= r
print(g)
```



모범 답안  
```
a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

for i in range(1, n):
  a = a*r

print(a)
```
