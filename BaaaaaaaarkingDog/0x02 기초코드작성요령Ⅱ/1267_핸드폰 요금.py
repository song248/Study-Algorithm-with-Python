n = int(input())
d_call = list(map(int, input().split()))
y_sum = 0
m_sum = 0
for i in d_call:
    y_sum += (i//30+1)*10
    m_sum += (i//60+1)*15
if y_sum < m_sum: print('Y', y_sum)
elif y_sum > m_sum: print('M', m_sum)
else:   print('Y', 'M', y_sum)