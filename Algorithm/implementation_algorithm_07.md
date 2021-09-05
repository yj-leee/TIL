```
lock = [[1,1,1],[1,1,0],[1,0,1]]
key = [[0,0,0],[1,0,0],[0,1,1]]

start = len(key) - 1 #2
end = start + len(lock) #4
expendSize = len(lock) + start * 2 #7

for a in range(0, 4): # 회전
    for i in range(end):
        for j in range(end):
            if check(i, j, key, lock, expendSize, start, end):
                return True
    key = rotation(key)
return False
```
