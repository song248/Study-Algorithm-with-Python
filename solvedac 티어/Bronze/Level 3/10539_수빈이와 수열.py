n = int(input())
n_list = list(map(int, input().split()))
answer = []
for i in range(0, n):
    try:
        answer.append(n_list[-i-1]*(n-i) - n_list[-i-2]*(n-i-1))
    except:
        answer.append(n_list[-i-1]*(n-i))
answer.reverse()
for i in answer:
    print(i, end = ' ')