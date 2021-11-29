board = [list(map(int, input().split())) for _ in range(9)] 
maxi = 0
for i in range(len(board)):
    if maxi < max(board[i]):
        maxi = max(maxi, max(board[i]))
        x, y =  i+1, board[i].index(max(board[i]))+1
print(maxi)
print(x, y)