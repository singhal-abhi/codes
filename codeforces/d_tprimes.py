import math
n=input()
l=list(map(int,input().split()))
for i in l:
    n=math.sqrt(i)
    if(int(n)==n):
        n=int(n)
        for j in range(2,n):
            if(n%j==0):
                print("NO")
                break
        else:
            print("YES")
    else:
        print("NO")
