n, k = map(int,input().split())
ans = [[0]*7 for _ in range(2)]
room = 0

for _ in range(n):
    s, y = map(int, input().split())
    ans[s][y] += 1    

for i in ans:
    for j in i:
        if j%k != 0:    room += (j//k)+1
        else:    room += j//k
print(room)