for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    j=0
    s=[]
    for i in range(n):
        if(i%2==0):
            s.append(l[0])
            l.remove(l[0])
        else:
            s.append(l[-1])
            l=l[:-1]
    print(*s)
