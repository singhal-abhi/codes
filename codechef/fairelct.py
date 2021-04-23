for _ in range(int(input())):
    m,n=map(int,input().strip().split())
    ml=list(map(int,input().split()))
    nl=list(map(int,input().split()))
    c=0
    while(sum(ml)<=sum(nl)):
        if(c>m):
            print(-1)
            break
        ml.sort()
        nl.sort()
        ml[0],nl[-1]=nl[-1],ml[0]
        c+=1
    else:
        print(c)
