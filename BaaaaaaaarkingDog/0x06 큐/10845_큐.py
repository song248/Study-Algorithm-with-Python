from sys import stdin
qq = []
for _ in range(int(stdin.readline())):
    com = stdin.readline().split()
    if com[0] == 'push':
        qq.append(int(com[1]))
    elif com[0] == 'pop':
        if qq :    print(qq.pop(0))
        else:    print(-1)
    elif com[0] == 'front':
        if qq:    print(qq[0])
        else:    print(-1)
    elif com[0] == 'back':
        if qq:    print(qq[-1])
        else:    print(-1)
    elif com[0] == 'size':
        print(len(qq))
    elif com[0] == 'empty':
        if qq:    print(0)
        else:    print(1)