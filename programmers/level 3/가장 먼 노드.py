from collections import deque

def solution(n, edge):
    graph = [[]*(n+1) for _ in range(n+1)]
    for node in edge:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])
    visited = [0]*(n+1)
    visited[1] = 1
    qq = deque([1])
    
    while qq:
        n = qq.popleft()
        for i in graph[n]:
            if visited[i] == 0:
                visited[i] = visited[n]+1
                qq.append(i)
                
    return visited.count(max(visited))