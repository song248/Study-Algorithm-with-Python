a = int(input())
b = int(input())
c = int(input())
d = int(input())
sci = [a, b, c, d]
e = int(input())
f = int(input())
soc = [e, f]
sci.sort(reverse=True)
print(sum(sci[:3])+max(soc))