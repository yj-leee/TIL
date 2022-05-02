# dfs 깊이 우선 탐색이다 스택이랑 큐중에 뭐다? 큐다~, 큐는 뭐다? 선입 선출

n, m, v = int(input())
graph = [[] for _ in range(m)]
for i in m:
    a, b = int(input())
    graph[a].append(b)
    
print(graph)
    
    
    
    
