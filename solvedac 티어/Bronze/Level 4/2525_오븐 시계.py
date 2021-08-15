h, m = map(int, input().split())
time = int(input())
print(((h+time//60) + (m+time%60)//60)%24, (m+time%60)%60)


h,m=map(int,input().split())
t=h*60+m+int(input())
print(t//60%24,t%60)