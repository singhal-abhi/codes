t=int(input())
while(t):
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    n=[]
    for i in l:
        if i not in n:
            n.append(i)
    print(*n)
