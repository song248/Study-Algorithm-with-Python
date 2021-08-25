from sys import stdin

for _ in range(int(stdin.readline().strip())):
    st = stdin.readline().strip()
    left, right = [], []
    for i in st:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    print(''.join(left)+''.join(reversed(right)))