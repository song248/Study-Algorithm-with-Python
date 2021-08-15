n, m = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque

def bfs(x, y):
    qq = deque()
    qq.append((x, y))
    cnt = 0
    while qq:
        cnt += 1
        if cnt == 100: break
        for ho in miro:
            print(ho)
        print('-'*50)

        x, y = qq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                print("** nx: {}, ny: {} / miro: {}".format(nx, ny, miro[nx][ny]))
                if miro[nx][ny] == 1:
                    miro[nx][ny] = miro[x][y]+1
                    qq.append((nx, ny))
        print(' ')

bfs(0, 0)
print(miro[n-1][m-1])

# ----------------------------------------------------------------------
# 책 풀이
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    #큐가 빌때까지
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]


print(bfs(0,0))