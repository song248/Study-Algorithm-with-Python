n = int(input())
score = list(map(int, input().split()))
d = max(score)
for i in range(len(score)):
    score[i] = score[i]/d*100
print(sum(score)/n)