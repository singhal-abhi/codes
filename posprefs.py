"""wrong answer""""
t=int(input())
while(t):
    t-=1
    n,k=map(int,input().split())
    l=[1,2]
    c=2
    if(n==1):
        print(1)
        continue
    if(n==2):
        if(k==1):
            print(1,-2)
        else:
            print(1,2)
        continue
    for i in range(3,n+1):
        if(c<k and n!=k):
            if(sum(l)>0):
                l.append(-i)
            else:
                c+=1
                l.append(i)
        elif(n==k):
            l.append(i)
        else:
            l.append(-i)
    print(*l)
