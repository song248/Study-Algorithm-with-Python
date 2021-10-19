stack = []
s = input()
try:
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        elif s[i] == ')':
            if stack[-1] == '(':
                stack.pop()
                stack.append(2)
            else:
                tmp = 0
                for j in range(len(stack) - 1, -1, -1):
                    if stack[j] == '(':
                        stack[-1] = tmp * 2
                        break
                    else:
                        tmp += stack[j]
                        stack = stack[:-1]
        elif s[i] == ']':
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                tmp = 0
                for j in range(len(stack) - 1, -1, -1):
                    if stack[j] == '[':
                        stack[-1] = tmp * 3
                        break
                    else:
                        tmp += stack[j]
                        stack = stack[:-1]
    print(sum(stack))
except:
    print(0)