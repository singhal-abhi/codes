for _ in range(int(input())):
    r=int(input())
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(len(l)):
        if(l[i]>=r):
            print(i+1)
            break
