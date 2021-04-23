for _ in range(int(input())):
    s,k=map(int,input().split())
    l=(list(map(int,input().split())))
    s=sum(l)
    l=min(l)
    if(s//k!=(s-l)//k):
        print(s//k)
    else:
        print(-1)
