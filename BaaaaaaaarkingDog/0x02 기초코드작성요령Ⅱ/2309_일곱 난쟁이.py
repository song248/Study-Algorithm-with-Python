aaa = [int(input()) for _ in range(9)]
aaa.sort()
total = sum(aaa)

for i in aaa:
    for j in aaa:
        total -= (i+j)
        if total == 100:
            ans_a, ans_b = i, j
            break
        else:   total = sum(aaa)
aaa.remove(ans_a)
aaa.remove(ans_b)
for i in aaa:   print(i)

# ----------------------------------------

aaa = [int(input()) for _ in range(9)]
aaa.sort()
total = sum(aaa)

for i in aaa:
    for j in aaa:
        if i+j == sum(aaa)-100:
            aaa.remove(i)
            aaa.remove(j)
			break
for i in aaa:   print(i)