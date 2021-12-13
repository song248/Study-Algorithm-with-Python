axis = 0
m = [0]*4
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        axis += 1
	elif x > 0 and y > 0:
		m[0] += 1
	elif x < 0 and y > 0:
		m[1] += 1
	elif x < 0 and y < 0:
		m[2] += 1
	else:
		m[3] += 1
print('Q1: {}'.format(m[0]))
print('Q2: {}'.format(m[1]))
print('Q3: {}'.format(m[2]))
print('Q4: {}'.format(m[3]))
print('AXIS: {}'.format(axis))