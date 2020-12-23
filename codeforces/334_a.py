n=int(input())
l=[]
for i in range(1,n**2+1):
    l.append((i,n**2-i+1))
for j in range(n):
    for i in range(n//2):
        print(*l[0],end=" ")
        l.remove(l[0])
    print()
