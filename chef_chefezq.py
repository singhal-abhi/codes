t=int(input())
while(t):
    t-=1
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(n-1):
        if(l[i]<k):
            print(i+1)
            break
        l[i+1]+=(l[i]-k)
        l[i]=k
    else:
        
        print(l[n-1]//k+1+l.count(k))
