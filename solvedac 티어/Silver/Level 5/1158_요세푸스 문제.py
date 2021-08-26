n, k = map(int, input().split())
n_list = [i for i in range(1, n+1)]
ans, c = [], k-1

while len(n_list):
    if c >= len(n_list):
        c = c % len(n_list)
    else:
        ans.append(str(n_list.pop(c)))
        c += k-1
 
print('<{}>'.format(', '.join(ans)))