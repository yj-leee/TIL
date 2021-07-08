


>6088 : [기초-종합] 수 나열하기1(py)

```
a,b,c = input().split()

a = int(a)
d = int(b)
n = int(c)

n = a+(n-1)*d
print(n)
```



모범 답안  
```
a,d,n=input().split()

a=int(a)
d=int(d)
n=int(n)

s=a
for i in range(2, n+1):
   s+=d

print(s)
```
