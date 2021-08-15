

> 2중 for문 말고 O(N)으로 풀 수 있는 방법
 

포인트
A가 특정 무게를 골랐다면 해당 무게의 공의 갯수 * 해당 무게의 공을 제외한 나머지 공의 개수하면 경우의 수가 나온다.

```
import time

start_time = time.time()
N, M = map(int, input().split())
K = list(map(int, input().split()))

# 무게를 담을 리스트
array = [0] * 11

for i in K:
    array[i] += 1

result = 0
for i in range(1, M+1):
    N -= array[i]
    result += array[i] * N
print(result)
end_time = time.time()
print("프로그램 수행 시간: ", end_time - start_time)

```
