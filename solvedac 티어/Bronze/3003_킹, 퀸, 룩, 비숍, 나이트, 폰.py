piece = [1, 1, 2, 2, 2, 8]
answer = list(map(int, input().split()))
for i in range(len(piece)):
    print(piece[i] - answer[i], end = ' ')