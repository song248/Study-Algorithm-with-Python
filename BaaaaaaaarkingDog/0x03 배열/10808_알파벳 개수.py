s = input()
alpha = [0]*26
for i in s:    alpha[ord(i)-97] += 1
for a in alpha: print(a, end = ' ')