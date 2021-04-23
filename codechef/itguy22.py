import math
for _ in range(int(input())):
    a,b=map(int,input().split())
    if(a==b):
        print(0)
        continue
    l=a*b//math.gcd(a,b)
    print(l//a+l//b-2)
