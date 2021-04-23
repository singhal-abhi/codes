for _ in range(int(input())):
    n=int(input())
    f=list(map(int,input().split()))
    c=list(map(int,input().split()))
    '''d=0
    while(n>0):
        m=1000000000
        g=0
        for i in range(len(f)):
            if(m>c[i] and c[i]!=0):
                m=c[i]
                if(f[i]>g):
                    g=f[i]
            n-=m*g
            d+=m*g
            f.remove(f[i])
            c.remove(c[i])
    print(d)'''
    d={}
    l=[]
    for i in range(n):
        l.append((c[i],f[i]))
    l.sort(reverse=True)
    while True:
        m=min(c[i])
