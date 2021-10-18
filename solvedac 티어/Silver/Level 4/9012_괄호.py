for i in range(int(input())):
    word = input()
    stack = []
    for s in word:
        if not stack:    
            stack.append(s)
        else:
            if s == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
    if not stack:
        print('YES')
    else:
        print('NO')