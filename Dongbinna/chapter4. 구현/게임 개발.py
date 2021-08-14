n, m = map(int, input().split())
x, y, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 첫번째 위치도 방문으로 간주하고 방문했으니까 1로 변경
matrix[x][y] = 1
# 첫번째 칸도 방문으로 간주해야 하니까 1부터 시작
cnt = 1
turn = 0

# 북 동 남 서 (0, 1, 2, 3)
# 반시계 회전이니가 1씩 감소하는 형태로
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True: 
    d -= 1
    if d < 0:
        d = 3
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx <= n and 0 <= ny <= m:
        if matrix[nx][ny] == 0:
            matrix[nx][ny] = 1
            x, y = nx, ny
            cnt += 1
            turn = 0
        else:
            turn += 1
        
        if turn == 4:
            nx = x - dx[d]
            ny = y - dy[d]
            if matrix[nx][ny] == 0:
                x, y = nx, ny
            else:
                break
            turn = 0
    else:
        print('out of range')
print(cnt)