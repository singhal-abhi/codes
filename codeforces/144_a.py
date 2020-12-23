#for submission
n=int(input())
l=list(map(int,input().split()))
mx=max(l)
mn=min(l)
c=1-1
mx=l.index(mx)
if(l.index(mn)<mx and mn not in l[mx:]):
    c=-1
l.reverse()
mn=l.index(mn)
print(mx+mn+c)
