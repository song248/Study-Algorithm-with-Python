from sys import stdin
qq = []
cnt = 0
for _ in range(int(stdin.readline())):
    com = stdin.readline().split()
    if com[0] == 'push':
        qq.append(com[1])
    elif com[0] == 'pop':
        if len(qq) > cnt:
            print(qq[cnt])
            cnt += 1
        else: print(-1)
    elif com[0] == 'size':
        print(len(qq)-cnt)
    elif com[0] == 'empty':
        if len(qq) == cnt: 
            print(1)
            cnt = 0
            qq = []
        else:   
            print(0)
    elif com[0] == 'front':
        if len(qq) > cnt: 
            print(qq[cnt])
        else: 
            print(-1)
    elif com[0] == 'back':
        if len(qq) > cnt: 
            print(qq[-1])
        else: 
            print(-1)