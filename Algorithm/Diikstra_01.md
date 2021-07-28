

>다익스트라 최단 경로 알고리즘

특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
'음의 간선'이 없을 때 정상적으로 동작. 음의 간선이란 0보다 작은 값을 가지는 간선임
현실세계는는 음의 간선으로 표현되지 않으므로 다익스트라 알고리즘은 실제로 GPS 소프트웨어의 기본 알고리즘으로 채택되곤 한다.

1. 출발 노드 설정
2. 최단 거리 테이블을 초기화
3. 방문하지 않은 노드 중에서 최단 거리가 짧은 노드 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다
5. 3-4번을 반복한다

방문하지 않은 노드 중에서 현재 최단거리가 가장 짧은 노드를 확인해서 테이블에 갱신!! 이 핵심인듯하다.

1. 구현하기 쉽지만 느리게 동작하는 코드
2. 구현하기 조금 더 까다롭지만 빠르게 동작하는 코드..

그러니까 두가지 방법이 있는데 첫번째 방법보다 두번째 방법이 더 효율적이니까 알아둬라


## step 1. 노드 정보, 방문 정보, 최단거리 테이블 리스트 만들어주기
```
import sys

input = sys.stdin.readline

# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())

# 시작 노드 번호를 입력받기
start = int(input())

# 0번은 취급하지 않기위해 n+1길이만큼 생성
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n+1)]

# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False]* (n+1)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력 받기
for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
```

input data
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

출력 결과 
```
graph = [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]
visited = [False, False, False, False, False, False, False]
distance = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
```

## step 2. 노드 정보, 방문 정보, 최단거리 테이블 리스트 만들어주기


```
# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    # 가장 최단 거리가 짧은 노드(인덱스)
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
        return index

# 해당 노드를 거쳐 다른 노드로 가는 비용을 계산, 최단 거리 테이블 갱신
def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해서 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한 이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

```





