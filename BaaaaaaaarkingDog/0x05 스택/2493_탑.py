n = int(input())
n_list = list(map(int, input().split()))
stack, answer = [], []
for i in range(n):
    while stack:
        if stack[-1][1] > n_list[i]:
            answer.append(stack[-1][0]+1)
            break
        else: 
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append((i, n_list[i]))
for i in answer:
    print(i, end = ' ')