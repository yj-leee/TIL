

> 규칙 

동전을 순서대로 정렬하고 하나씩 추가하며 더해갔을 때, 구하려고자 하는 target의 값보다  
새로 추가되는 동전보다 크면 출력한다!


```
import time

start_time = time.time()
N = int(input())
coins = list(map(int, input().split()))

coins.sort()
target = 1

for i in coins:
    if target < i:
        break
    target += i
print(target)

end_time = time.time()
print("프로그램 수행 시간: ", end_time - start_time)

```



