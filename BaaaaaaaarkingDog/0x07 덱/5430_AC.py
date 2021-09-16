from sys import stdin
from collections import deque

for _ in range(int(stdin.readline())):
    p = stdin.readline().rstrip()
    n = int(stdin.readline())
    arr = stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)

    rev, flag = 0, 0
    flag = 0
    if n == 0:
        queue = []
    for i in p:
        if i == 'R':
            if rev == 0:
                rev = 1
            else:
                rev = 0
        elif i == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev == 1:
            queue.reverse()
        print("[" + ",".join(queue) + "]")