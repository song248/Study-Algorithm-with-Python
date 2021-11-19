def solution(n, results):
#     이긴 사람 사전, 진 사람 사전
    win, lose = {}, {}
    for i in range(1, n+1):
#         각각 value는 집합 set
        win[i], lose[i] = set(), set()
    
#     dict update는 두 사전의 병합을 의미
    for i in range(1, n+1):
        for battle in results:
            if battle[0] == i:
                win[i].add(battle[1])
            if battle[1] == i:
                lose[i].add(battle[0])
        for winner in lose[i]:
            win[winner].update(win[i])
        for loser in win[i]:
            lose[loser].update(lose[i])
            
    answer = 0
    for i in range(1, n+1):
#         이기고 지는 경우의 합이 본인 제외 수와 같아야 함
        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1
    return answer