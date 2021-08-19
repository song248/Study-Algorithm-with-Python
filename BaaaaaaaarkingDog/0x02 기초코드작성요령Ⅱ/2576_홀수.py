aaa = [int(input()) for _ in range(7)]
mini, sum = 100, 0
for i in aaa:
    if i%2 == 1:    
        sum += i
        if i < mini:
            mini = i
if sum != 0:
    print(sum)
    print(mini)
else:
    print(-1)
	
# ------------------------------------------------------------
	
aa = [i for i in [int(input()) for _ in range(7)] if i%2 == 1]
if aa:
    print(sum(aa))
    print(min(aa))
else:    print(-1)