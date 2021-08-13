L, P = map(int, input().split())
gisa = list(map(int, input().split()))
baam = L*P
for i in gisa:
    print(i-baam, end=' ')