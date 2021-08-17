n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
b_list = list(map(int, input().split()))

for i in range(m):
    if b_list[i] in a_list:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

# --------------------------------------------------
# 이진탐색으로 풀기

def b_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
a_list = list(map(int, input().split()))
a_list.sort()
m = int(input())
b_list = list(map(int, input().split()))

for i in b_list:
    result = b_search(a_list, i, 0, n-1)
    if result != None:  print('yes', end = ' ')
    else: print('no', end = ' ')