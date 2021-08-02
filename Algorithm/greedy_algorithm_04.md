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
