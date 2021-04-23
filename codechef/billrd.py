for _ in range(int(input())):
    n,k,x,y=map(int,input().split())
    xi=yi=1
    b=(0,n)
    if(x==y):
        print(n,n)
        continue

    while(k>0):
        a=abs(x-y)
        if(x in b and y in b):
            break
        x+=xi
        y+=yi
        if(x in b or y in b):
            k-=1
            if(x in b):
                xi=xi*-1
            if(y in b):
                yi=yi*-1
    print(x,y)
