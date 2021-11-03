a = int(input())
b = int(input())
c = int(input())

n_list = [0]*10
for i in str(a*b*c):
    n_list[int(i)] += 1
for i in n_list:
    print(i)

------------------------------

a = int(input())
b = int(input())
c = int(input())
d = str(a*b*c)
for i in range(10):
  print(d.count('{}'.format(i)))