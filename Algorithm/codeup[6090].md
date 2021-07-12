
>6090 : [기초-종합] 수 나열하기3(py) 해결

```
a, m, d, n = input().split()

a = int(a)
m = int(m)
d = int(d)
n = int(n)


for i in range(1, n):
    a = (a * m) + d
    
print(a)
```



모범 답안  
```
a, m, d, n = input().split()

a = int(a)
m = int(m)
d = int(d)
n = int(n)

for i in range(1, n) :
  a = a*m+d

print(a)

```
