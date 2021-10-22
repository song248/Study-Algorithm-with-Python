n, k = map(int, input().split())
n_list = []
for i in range(1, int(n**(1/2)) + 1):
    if (n % i == 0):
        n_list.append(i) 
        if ( (i**2) != n) : 
            n_list.append(n // i)
n_list.sort()
try:    print(n_list[k-1])
except:    print(0) 