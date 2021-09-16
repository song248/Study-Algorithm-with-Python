from collections import deque

n, m  = map(int, input().split())
ck = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])
cnt = 0

for i in ck:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            # 2번 연산 - 앞에서 빼기
            if dq.index(i) < len(dq)/2:
                while dq[0] != i:
                    dq.append(dq.popleft())
                    cnt += 1
            # 3번 연산 - 뒤에서 빼기
            else:
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    cnt += 1
print(cnt)