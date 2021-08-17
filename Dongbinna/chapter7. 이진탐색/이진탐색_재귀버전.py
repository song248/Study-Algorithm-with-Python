def bianry_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return bianry_search(array, target, start, mid-1)
    else:
        return bianry_search(array, target, mid+1, end)

n, target = map(int, input().split())
array = list(map(int, input().split()))

result = bianry_search(array, target, 0, n-1)
if result == None:
    print('None')
else: 
    print(result+1)