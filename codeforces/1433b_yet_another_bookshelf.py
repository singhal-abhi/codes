t=int(input())
while(t):
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    d={}
    for i in l:
        d[i]=d.get(i,0)+1
    f=l.index(1)
    l.reverse()
    f=n-l.index(1)-f
    print(f-d[1])
