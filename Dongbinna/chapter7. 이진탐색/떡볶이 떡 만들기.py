n, m = map(int, input().split())
ddeok = list(map(int, input().split()))

start, end = 0, max(ddeok)
answer = 0

while start <= end:
    total, mid = 0, (start+end)//2
    for i in ddeok:
        if i > mid:
            total += i - mid
    if total < m:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)