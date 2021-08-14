n, k = map(int, input().split())
cnt = 0

while True:
    if n%k == 0:
        n = n//k
    else:
        n -= 1
    cnt += 1
    if n<k:
        break
while n>1:
    n -= 1
    cnt += 1

print(cnt)

# 엄청 큰 수(worst case) -> n이 k의 배수가 되도록 한번에 처리하는 방법 찾기

n, k = map(int, input().split())
result = 0
while True:
    target = (n//k)*k
    result += (n-target)
    n = target
    if n < k:
        break
    result += 1
    n //= k
result += (n-1)
print(result)