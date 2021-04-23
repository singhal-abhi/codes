for _ in range(int(input())):
    n=int(input())
    l=sorted(list(map(int,input().split())))
    try:
        x=l[0]
        y=l[l.count(x)]
        z=l[-1]
        print(abs(x-z)+abs(x-y)+abs(y-z))
    except:
        print(0)
