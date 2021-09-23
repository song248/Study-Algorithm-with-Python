while True:
    str_in = input()
    null_chk = 0
    chk = []
    if str_in == '.':    break
    for s in str_in:
        if s == '[' or s == '(':
            chk.append(s)
        elif s == ']':
            if chk and chk[-1] == '[':
                chk.pop()
            else:
                null_chk = 1
                break
        elif s == ')':
            if chk and chk[-1] == '(':
                chk.pop()
            else:
                null_chk = 1
                break
    if null_chk == 0 and not(chk):
        print('yes')
    else:
        print('no')