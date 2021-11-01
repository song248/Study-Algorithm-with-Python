from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
qq = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            qq.append((i,j))
def bfs():
    while qq:
        x, y = qq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if box[nx][ny] == 0:
                    box[nx][ny] = box[x][y] + 1
                    qq.append((nx, ny))
bfs()
chk = 0
result = -2
for i in box:
    for j in i:
        if j == 0:
            chk = 1
        result = max(result, j)
if chk == 1:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)