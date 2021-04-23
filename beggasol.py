for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    f=l[0]
    i=1
    d=0
    while(f):
        d+=1
        f-=1
        try:
            f+=l[i]
        except:
            break
        i+=1
    print(d+f)
