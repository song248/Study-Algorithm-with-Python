answer = list(map(int, input().split()))
total = 0
for i in answer:
    total += i**2
print(total%10)

answer = [i**2 for i in map(int, input().split())]
print(sum(answer)%10)