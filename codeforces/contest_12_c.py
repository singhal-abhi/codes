n=int(input())
l=list(map(int,input().split()))
m=0
if(n<3):
    print(sum([i**2 for i in l]))
    exit()
x=max(l)
for j in range(n):
    r = [sum(l[i : : 2]) for i in range(2)]
    if(m<r[0]**2+r[1]**2):
        m=r[0]**2+r[1]**2
    l.remove(x)
    l=l[1:]+[l[0],x]
print(m)
