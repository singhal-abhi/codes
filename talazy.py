t=int(input())
import math
while(t):
    t-=1
    n,b,m=map(int,input().split())
    s=0
    while True:
        s+=m*math.ceil(n/2)
        n=n//2
        m=m*2
        s+=b
        if(n==1):
            s+=m
            break
    print(s)
