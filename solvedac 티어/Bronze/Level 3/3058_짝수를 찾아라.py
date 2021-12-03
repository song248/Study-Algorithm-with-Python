for _ in range(int(input())):
    n, mini = 0, 100
    n_list = list(map(int, input().split()))
    for i in n_list:
        if i%2 == 0:
            n += i
            mini = min(i, mini)
    print(n, mini)