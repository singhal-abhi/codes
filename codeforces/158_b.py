n=int(input())
l=list(map(int,input().split()))
f=l.count(4)
c=f
o=l.count(1)
t=l.count(3)
s=min(o,t)
o-=s
t-=s
c+=s
s=l.count(2)
c+=s//2
s=s%2
if(o==0):
    c+=t
    t=0
c+=abs(-(-(o+s*2+t*3)//4))
print(c)