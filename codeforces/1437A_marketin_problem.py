t=int(input())
while(t):
    l=list(map(int,input().split()))
    if(l[1]/2<l[0]):
        print("YES")
    else:
        print("NO")
    t-=1
