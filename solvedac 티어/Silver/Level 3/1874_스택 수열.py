import sys

cnt, chk = 0, 1
stk = []
result = ''

for _ in range(int(sys.stdin.readline())):
    target = int(sys.stdin.readline())
    while cnt < target:
        cnt += 1
        stk.append(cnt)
        result += '+'
    if stk[-1] == target:
        result += '-'
        stk.pop()
    else: chk = 0
if chk == 0:    print('NO')
else:    
    for i in result:    print(i)