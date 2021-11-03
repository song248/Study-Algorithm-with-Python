n = int(input())
new_n, cnt = n, 0
while True:
    a = new_n//10
    b = new_n%10
    c = (a+b)%10
    new_n = b*10 + c
    cnt += 1
    if n == new_n:
        break
print(cnt)