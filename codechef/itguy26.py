import math
for _ in range(int(input())):
    t=n=int(input())
    s=0
    while(n>0):
        s+=math.factorial(n%10)
        n=n//10
        if(s>t):
            break
    if(s==t):
        print(1)
    else:
        print(0)
