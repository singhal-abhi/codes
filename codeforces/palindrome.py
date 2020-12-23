def c(s):
    if(s==s[::-1]):
        return True
    else:
        return False
n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(input())
for i in l:
    if not (c(i) or i[::-1] in l):
        l.remove(i)
m=0
for i in l:
    if c(i):
        if(m==0):
            n=i
            m=1
        else:
            l.remove(i)
s=[0]*len(l)
j=0
for i in l:
    if not c(i):
        s[j]=i
        s[-j-1]=i[::-1]
        try:
            l.remove(i)
            l.remove(i[::-1])
        except:
            pass
try:
    s[s.index(0)]=n
except:
    pass
print(*s,sep="")
