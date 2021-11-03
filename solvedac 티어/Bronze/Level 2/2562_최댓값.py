aaa = []
for _ in range(9):
    aaa.append(int(input()))
print(max(aaa))
print(aaa.index(max(aaa))+1)