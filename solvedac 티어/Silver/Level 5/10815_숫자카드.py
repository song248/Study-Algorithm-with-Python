n = int(input())
card = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
card.sort()

def bin_search(card, target, start, end):
    if start > end:    return 0
    mid  = (start+end)//2
    if card[mid] == target:
        return 1
    elif card[mid] > target:
        end = mid - 1
    else:
        start = mid+1
    return bin_search(card, target, start, end)

answer = []
for i in range(m):
    answer.append(bin_search(card, check[i], 0, n-1))
answer = " ".join(map(str, answer))
print(answer)