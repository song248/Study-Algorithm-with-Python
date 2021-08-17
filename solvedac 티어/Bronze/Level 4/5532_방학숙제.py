L = int(input())    # 방학일수
A = int(input())    # 국어 풀 페이지 수
B = int(input())    # 수학 풀 페이지 수
C = int(input())    # 국어 하루에 풀 수 있는 수
D = int(input())    # 수학 하루에 풀 수 있는 수
print(int(L - max(A/C, B/D)))