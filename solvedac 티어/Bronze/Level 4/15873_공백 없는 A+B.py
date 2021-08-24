a = input()
if a[-1] == '0':
    if a[-2] == '1':
        b = a[-2:]
        c = "".join(reversed(a[-3::-1]))
    else:
        b = a[-1]
        c = "".join(reversed(a[-2::-1]))
else:
    b = a[-1]
    c = "".join(reversed(a[-2::-1]))
print(int(b)+int(c))