
```
import heapq


food_times = [8, 6, 4]
k = 15

# (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
q = []
for i in range(len(food_times)):
    heapq.heappush(q,(food_times[i], i + 1))

# 가장 적은 시간이 걸리는 음식을 뺀다
min_q = heapq.heappop(q)[0]

# K 를 가장 적은 시간이 걸리는 음식을 먹는 시간만큼 빼준다.
# 가장 적은 시간이 걸리는 음식을 먹는 시간은 음식의 계수에 비례한다.
length = len(food_times)

min_t = length * min_q

print(min_q)
print(min_t)

k = k - min_t

# 남은 음식을 음식의 번호 기준으로 정렬한다
result = sorted(q, key =lambda x: x[1])
print(result)

# 남은 시간 번째에 있는 음식의 번호를 출력한다.
# 남은 시간이 남은 음식보다 큰 경우 다시 1번 음식으로 돌아가므로, 나머지번째에
# 있는 음식의 번호를 출력하면 된다.
print(result[1][1])

"""예외 사항

전체 음식을 먹는 시간보다 k가 크거나 같다면 -1이 출력된다.

"""
```


```
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    # 가장 적은 시간이 걸리는 음식을 먹기 위한 시간
    min_t = 0
    # 직전까지 사용한 시간
    total_t = 0
    # 남은 음식의 개수
    length = len(food_times)

    # 남은 시간이 다음 먹을 음식의 시간보다 작은 경우 출력
    while min_t <= k:
        # 가장 적은 시간이 걸리는 음식을 뺀다
        min_q = heapq.heappop(q)[0]

        # 가장 적은 시간이 걸리는 음식을 먹는 시간을 구한다
        min_t = length * min_q

        # 남은 시간, 음식의 개수
        k = k - min_t
        length -= 1

    # 남은 음식을 음식의 번호 기준으로 정렬한다
    result = sorted(q, key =lambda x: x[1])
    print(result[k % length][1])



solution([8, 6, 4], 15)
```
