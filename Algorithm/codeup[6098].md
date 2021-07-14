>6098 : [기초-리스트] 성실한 개미(py)

```
d = []
for i in range(10):
    d.append([])
    d[i] = list(map(int, input().split()))

# 개미의 위치
x = 1
y = 1

while True:
    if d[x][y] == 0:
        d[x][y] = 9
        y += 1

    elif d[x][y] == 1:
        y -= 1
        d[x][y] = 9
        x += 1

    elif d[x][y] == 2:
        d[x][y] = 9
        break;

    # 길이 없을 때
    if x >= len(d[x])-1:
        break;
    elif y >= len(d[y])-1:
        x += 1


for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()
```


모범 답안  
```
m=[]
for i in range(12) :
  m.append([])
  for j in range(12) :
    m[i].append(0)

for i in range(10) :
  a=input().split()
  for j in range(10) :
    m[i+1][j+1]=int(a[j])

x = 2
y = 2
while True :
  if m[x][y] == 0 :
    m[x][y] = 9
  elif m[x][y] == 2 :
    m[x][y] = 9
    break

  if (m[x][y+1]==1 and m[x+1][y]==1) or (x==9 and y==9) :
    break

  if m[x][y+1] != 1 :
    y += 1
  elif m[x+1][y] != 1 :
    x += 1
    

for i in range(1, 11) :
  for j in range(1, 11) :
    print(m[i][j], end=' ')
  print()
```
