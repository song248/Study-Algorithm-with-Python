n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

def dfs(x, y):
    print(matrix)
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if matrix[x][y] == 0:
        matrix[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

for i in range(n):
    for j in range(m):
    if dfs(i, j) == True:
        print(i, j)
        cnt += 1
print(cnt)