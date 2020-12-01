q=int(input())
import math
while(q):
    q-=1
    t=n=int(input())
    c=0
    while True:
            i=math.sqrt(t)
            if(i%1==0):
                t=n-t
                n=t
                c+=1
                if(t==0):
                    break
            else:
                t-=1
    print(c)
