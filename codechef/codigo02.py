for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=sorted(l)
    c=0
    cp=0
    for i in s:
        a=l.index(i)
        c+=abs(cp-a)
        cp=a
    print(c)
