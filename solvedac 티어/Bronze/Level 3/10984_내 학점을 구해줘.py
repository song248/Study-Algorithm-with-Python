for _ in range(int(input())):
    n = int(input())
    rt, total = 0, 0
    for _ in range(n):
        c, g = map(float, input().split())
        rt += c
        total += c*g
    print(int(rt), round(total/rt, 1))