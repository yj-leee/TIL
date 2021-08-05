
```
s = input()

result = s[0]
for i in range(1, len(s)):
    if int(result) * int(s[i]) > int(result) + int(s[i]):
        result = result * int(s[i])
    else:
        result = int(result) + int(s[i])
print(result)

```



```
import time

start_time = time.time()
num_str = input()
result = int(num_str[0])

for i in range(1, len(num_str)):
    # 0 또는 1 인 경우에는 더하는게 효율적
    if int(num_str[i]) < 2 or result < 2:
        result += int(num_str[i])
    else:
        result *= int(num_str[i])
print(result)

end_time = time.time()
print("프로그램 수행 시간: ", end_time - start_time)
```
