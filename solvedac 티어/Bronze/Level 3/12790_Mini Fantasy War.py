for _ in range(int(input())):
    stat = list(map(int, input().split()))
    hp = stat[0] + stat[4]
    if hp < 1:    hp = 1
    mp = stat[1] + stat[5]
    if mp < 1:    mp = 1
    at = stat[2] + stat[6]
    if at < 0:    at = 0
    df = stat[3] + stat[7]
    print(hp + 5*mp + 2*at + 2*df)