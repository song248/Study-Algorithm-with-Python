# 완전탐색 - 브루트포스
n = int(input())
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            tmp = str(i)+str(j)+str(k)
            if '3' in tmp:
                cnt += 1
print(cnt)