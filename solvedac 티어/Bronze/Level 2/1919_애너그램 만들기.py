a = input()
b = input()
same = 0

a_list = [0]*26
for i in a:    a_list[ord(i)-97] += 1
b_list = [0]*26
for i in b:    b_list[ord(i)-97] += 1
for i in range(26):    same += abs(a_list[i] - b_list[i])
print(same)