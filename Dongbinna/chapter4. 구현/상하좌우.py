n = int(input())
matrix = list(input().split())

now = [1, 1]
dx = [0, 0, -1, 1]
dy = [-1,1, 0, 0]
move = ['L', 'R', 'U', 'D']

for mat in matrix:
    for i in range(4):
        if mat == move[i]:
            cx = now[0] + dx[i]
            cy = now[1] + dy[i]
            if 1 <= cx <= n and 1 <= cy <= n:
                now[0] = cx
                now[1] = cy
print(now[0], now[1])