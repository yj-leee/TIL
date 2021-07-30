
> 서로소 집합 자료구조

1. union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A,B 를 확인한다.
2. A 와 B의 루트노드를 각각 찾는다.
3. A'를 B'의 부모노드로 설정한다(찾은 루트노드 중에서 더 번호가 작은 원소가 부모 노드가 되도록 한다.)
4. 모든 union 연산을 처리할 때까지 과정을 반복한다.

```
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (v + 1)

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')
print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
```
