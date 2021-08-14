s = input()
s_alpa = []
s_num = []
answer = ''

for i in s:
    if 65 <= ord(i) <= 90:
        s_alpa.append(ord(i))
    else:
        s_num.append(int(i))

s_alpa.sort()
for ss in s_alpa:
    answer += chr(ss)
answer += str(sum(s_num))
print(answer)

# --------------------------------

data = input()
result = []
value = 0

# isalpha()
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()
if value == 0:
    if '0' in data:
        result.append(str(value))
else:
    result.append(str(value))
print(''.join(result))