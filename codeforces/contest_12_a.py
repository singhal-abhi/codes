for _ in range(int(input())):
    n=int(input())
    c=0
    l=list(map(int,input().split()))
    l.sort()
    for i in range(n-1):
        if(l[i]+1==l[i+1]):
            c+=1
    if(c==0):
        print(1)
    else:
        print(2)
