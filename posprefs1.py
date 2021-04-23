t=int(input())
while(t):
    t-=1
    n,k=map(int,input().split())
    l=[]
    for i in range(1,n+1):
        if(i%2==0):
            l.append(i)
        else:
            l.append(-i)
    c=0
    s=0
    for i in l:
        s+=i
        if(s>0):
            c+=1
    if(k==n/2):
        pass
    elif(k<n/2):
        r=c-k
        for i in range(n-1,-1,-1):
            if(l[i]>0):
                l[i]*=(-1)
                r-=1
            if(r==0):
                break
    elif(k>n/2):
        r=k-c
        for i in range(n-1,-1,-1):
            if(l[i]<0):
                l[i]*=(-1)
                r-=1
            if(r==0):
                break
    print(*l)
