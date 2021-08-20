n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
x = int(input())
cnt,ll, rr = 0, 0, n-1
while ll < rr:
    tmp = n_list[ll] + n_list[rr]
    if tmp == x:
        cnt += 1
        rr -= 1
    elif tmp < x:
        ll += 1
    elif tmp > x:
        rr -= 1
print(cnt)        