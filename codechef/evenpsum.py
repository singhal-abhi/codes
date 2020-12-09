t=int(input())
while(t):
    t-=1
    a,b=map(int,input().split())
    c=0
    c=(a//2)*(b//2)
    c+=(-(-a//2)*-(-b//2))
    print(c)
