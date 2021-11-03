for _ in range(int(input())):
    nn = list(map(int, input().split()))
    avg = sum(nn[1:])/nn[0]
    cnt = 0
    for s in nn[1:]:
        if s > avg:    cnt+=1
    result = round(cnt/nn[0]*100, 3)
    print('%.3f'%result+'%' )