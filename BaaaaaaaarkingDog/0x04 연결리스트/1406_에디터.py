from sys import stdin
 
st = list(stdin.readline().strip())
tmp = []

for _ in range(int(stdin.readline().strip())):
    m  = stdin.readline().strip()
    if m[0] == 'L':
        if st:
            tmp.append(st.pop())
        else: continue
    if m[0] == 'D':
        if tmp:
            st.append(tmp.pop())
        else: continue
    if m[0] == 'B':
        if st:
            st.pop()
        else: continue
    if m[0] == 'P':
        st.append(m[2])
print(''.join(st)+''.join(reversed(tmp)))