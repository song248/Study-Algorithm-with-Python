n = int(input())
if n%400 == 0: print(1)
elif n%100 != 0 and n%4 == 0: print(1)
else: print(0)