from collections import deque

n, m = map(int, input().split())
paint = [list(map(int, input().split())) for _ in range(n)]
chk = [[0]*m for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
cnt, max_w = 0, 0

def bfs(x, y):
    w = 1
    qq = deque()
    qq.append((x,y))
    chk[x][y] = 1
    while qq:
        x, y = qq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if paint[nx][ny] == 1 and chk[nx][ny] == 0:
                    chk[nx][ny] = 1
                    qq.append((nx, ny))
                    w += 1
    return w              
for i in range(n):
    for j in range(m):
        if paint[i][j] == 1 and chk[i][j] == 0:
            cnt += 1
            max_w = max(max_w, bfs(i, j))
print(cnt)
print(max_w)