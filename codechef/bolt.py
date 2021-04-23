import math
for _ in range(int(input())):
    l=list(map(float,input().split()))
    c=1
    for i in l:
        c=c*i
    if round(100/c,2)<9.58:
        print("YES")
    else:
        print("NO")
