d1,n1,d2,n2,s=map(int,input().split())
i=1
while True:
    if(i>d1):
        s-=n1
    if(i>d2):
        s-=n2
    if(s<=0):
        break
    i+=1
print(i-1)
