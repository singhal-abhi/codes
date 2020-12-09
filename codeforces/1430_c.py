t=int(input())
while(t):
    t-=1
    n=int(input())
    d=[]
    l=[i for i in range(1,n+1)]
    for i in range(n):
        try:
            d.append((l[-2],l[-1]))
            l[-2]=-(-(l[-1]+l[-2])//2)

            l.remove(l[-1])
        except:
            pass
    d.reverse()
    print(l[0])
    for i in d:
        print(*i)
