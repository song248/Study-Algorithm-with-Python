from collections import deque
n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
qq = deque()
qq.append((0, 0))
while qq:
    x, y = qq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == '1':
                qq.append((nx, ny))
                maze[nx][ny] = int(maze[x][y])+1
print(maze[n-1][m-1])