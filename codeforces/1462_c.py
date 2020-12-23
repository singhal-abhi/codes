for _ in range(int(input())):
    s=input()
    n=int(s)
    if(n>49 or n<1):
        print(-1)
        continue
    a=[]
    s=0
    while(s<n):
        for i in range(9,0,-1):
            if(s+i<=n):
                s+=i
                a.append(i)
                break
    a.sort()
    print(*a,sep="")
