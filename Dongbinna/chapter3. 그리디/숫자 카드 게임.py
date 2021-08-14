n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_in_min = 0
for mat in matrix:
    if min(mat) > max_in_min:
        max_in_min = min(mat)
print(max_in_min)


# 책 풀이------------------------------------------------------------------------
# 이게 더 구린거 같은데...

n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result =  max(result, min_value)
print(result)
