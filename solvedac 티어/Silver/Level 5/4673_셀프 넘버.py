def func_d(n):
    if n < 10: return n*2
    elif n < 100: 
        tn = str(n)
        return n + int(tn[0]) + int(tn[1])
    elif n < 1000: 
        tn = str(n)
        return n + int(tn[0]) + int(tn[1]) + int(tn[2])
    elif n < 10000: 
        tn = str(n)
        return n + int(tn[0]) + int(tn[1]) + int(tn[2]) + int(tn[3])
    elif n == 10000: return 10010
    
d_list = []
for i in range(1, 10000):
    d_list.append(func_d(i))
for i in range(1, 10000):
    if i not in d_list: print(i)

# ----------------------------------------------------------------------
# 리스트는 연산 속도가 느림 => set 집합 자료형 이용
# 문자열 변환과 int형 연산의 속도 차이는 크지 않음

def d(a):
    if(a<10):
        return a+a
    elif(a<100):
        return a+a//10+a%10
    elif(a<1000):
        return a+a//100+(a%100)//10+a%10
    else:
        return a+a//1000+(a%1000)//100+(a%100)//10+a%10
a= set()
for i in range(10000):
    a.add(d(i))
for i in range(1,10000):
    if(i not in a):
        print(i)