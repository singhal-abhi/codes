for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for i in l:
        i+=k
        if(i%7==0):
            c+=1
    print(c)
