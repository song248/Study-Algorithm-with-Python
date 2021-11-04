cnt = 0
for _ in range(int(input())):
    s = input()
    for i in range(len(s)):
        if i != len(s)-1:
            if s[i] == s[i+1]:
                pass
            elif s[i] in s[i+1:]:
                break
        else:
            cnt += 1
print(cnt)