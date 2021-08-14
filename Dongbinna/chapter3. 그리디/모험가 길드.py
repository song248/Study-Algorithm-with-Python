n = int(input())
adv = list(map(int, input().split()))
adv.sort()

group = 0
cnt = 0

for i in adv:
    group += 1
    if i == group:
        cnt += 1
        group = 0

print(cnt)