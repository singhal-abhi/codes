n,m=map(int,input().split())
x=[list(map(int,input().split())) for i in range(n)]
y=[list(map(int,input().split())) for i in range(m)]
c=0
"""for i in range(n):
    for j in range(m):
        if(x[i][0]==y[j][1] and x[i][1]==y[j][0]):
            c+=1
            break"""
for i in x:
    i.reverse()
    if i in y:
        c+=1
        y.remove(i)
print(c)
