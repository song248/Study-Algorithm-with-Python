from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
atom = list(map(int, input().split()))

result = bisect_right(atom, x)-bisect_left(atom, x)
if  result == 0:    print(-1)
else:   print(result)