for _ in range(int(input())):
    n=int(input())
    for a in range(n):
        f=0
        s=1
        if(a==0):
            print(0)
            continue
        print("01",end="")
        for x in range(2,a+1):
            next=f+s
            print(next,end="")
            f=s
            s=next
        print()
