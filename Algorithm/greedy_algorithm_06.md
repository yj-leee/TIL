

```
import time

start_time = time.time()

s = str(input())
z_count = s.count('0')
o_count = s.count('1')
index_list = list()

if z_count >= o_count:
    for i in range(len(s)):
        if s[i] == '0':
            pass
        if s[i] == '1':
            if s[i-1] != s[i]:
                index_list.append(i)
else:
    for i in range(len(s)):
        if s[i] == '1':
            pass
        if s[i] == '0':
            if s[i-1] != s[i]:
                index_list.append(i)

print(len(index_list))
end_time = time.time()
print("프로그램 수행 시간: ", end_time - start_time)
```

> 깔끔한 코드 정리

```
import time

start_time = time.time()

# s[0]이 0이면 [1,0] 아니면 [0,1]

cnt = [0, 0]

s = list(map(int, input()))
prevNum = s[0]

if prevNum == 0:
    cnt[0] += 1
else:
    cnt[1] += 1

for i in range(1, len(s)):
    if prevNum != s[i]:
        cnt[s[i]] += 1
    prevNum = s[i]

print(min(cnt))
end_time = time.time()
print("프로그램 수행 시간: ", end_time - start_time)
```


