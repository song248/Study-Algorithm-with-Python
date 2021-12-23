n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))
cheap = price[0]
total = 0
for i in range(n-1):
    if cheap > price[i]:
        cheap = price[i]
    total += cheap * dis[i]
print(total)