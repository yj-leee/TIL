
내가 쓴 코드
```
def binary_search(array, target, start, end):

    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    else:
        return binary_search(array, target, mid + 1, end)

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()
for i in b:
    result = binary_search(a, i, 0, n)
    if result:
        print('yes', end=' ')
    else:
        print('no', end=' ')
```


```
n = int(input())
array = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))


for i in b:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
```
