t=int(input())
while(t):
    t-=1
    n,d=map(int,input().split())
    l=list(map(int,input().split()))
    a=0
    b=0
    for i in l:
        if(i<10 or i>79):
            a+=1
        else:
            b+=1
    print((-(-a//d))+(-(-b//d)))
