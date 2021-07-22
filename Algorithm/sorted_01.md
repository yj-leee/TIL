


내가 쓴 코드
```
n = int(input())
array = list(map(int, input().split()))

for i in range(1, n):
    array.append(int(input()))
    for j in range(i, 0, -1):
        if array[j] >= array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)
```

```
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')
```
