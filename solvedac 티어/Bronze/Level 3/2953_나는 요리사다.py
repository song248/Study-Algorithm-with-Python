cnt, score = 0, 0
for i in range(5):
    tmp =  sum(list(map(int, input().split())))
    if tmp > score:
        score = tmp
        cnt = i+1
print(cnt, score)