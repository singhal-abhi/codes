for _ in range(int(input())):
    n,r=map(int,input().split())
    a=list(map(int,input().split()))[:n]
    b=list(map(int,input().split()))[:n]
    x=0
    l=[]
    for i in range(n-1):
        x+=b[i]
        l.append(x)
        x=x-abs(a[i+1]-a[i])*r
        if(x<0):
            x=0
        #print(x)
    l.append(x+b[-1])
    print(max(l))
