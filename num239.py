for _ in range(int(input())):
    l,r=map(int,input().split())
    c=0
    for i in range(l,r+1):
        if(str(i%10) in "239"):
            c+=1
    print(c)
