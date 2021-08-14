n = input()
col = ord(n[0]) - 96
row = int(n[1])
cnt = 0
move  = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

for mm in move:
    cx = row + mm[1]
    cy = col + mm[0]
    if 1 <= cx <= 8 and 1 <= cy <= 8:
        cnt += 1
print(cnt)