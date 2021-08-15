from collections import deque

def BFS(graph, start, visited):
    qq = deque([start])
    visited[start] = True
    
    while qq:
        v = qq.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                qq.append(i)
                visited[i] = True
# 예제 그래프
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9
BFS(graph, 1, visited)