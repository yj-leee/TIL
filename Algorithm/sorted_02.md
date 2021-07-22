

내가 쓴 코드

```
n = int(input())

def setting(data):
    return data[1]

array = []
for i in range(n):
    data = input().split()
    array.append((data[0],data[1]))


result = sorted(array, key=setting)
for i in result:
    print(i[0], end=' ')
```

```
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))


array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
```
