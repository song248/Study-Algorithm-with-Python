n_list, total = [], 0
for _ in range(10):
    ne, ta = map(int, input().split())
    total -= ne
    n_list.append(total)
    total += ta
    n_list.append(total)
print(max(n_list))