'''
백트래킹(퇴각검색)
DFS(깊이 우선 탐색) 방식 기반으로, 불필요한 경우를 배제하며
원하는 해답에 도달할 때까지 탐색하는 전략
'''

n, m = map(int, input().split())

number_list = [1 + i for i in range(n)]
check_number = [False] * n
array = []
def back(x):
    if x == m:
        print(' '.join(map(str, array)))            
        return
            
    for i in range(n):
        if check_number[i]:
            continue
        array.append(number_list[i])
        check_number[i] = True

        back(x + 1)

        array.pop()         
        check_number[i] = False
back(0)    