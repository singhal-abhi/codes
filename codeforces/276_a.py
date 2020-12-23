n,t=map(int,input().split())
l=[]
for i in range(n):
    l.append(tuple(map(int,input().split())))
l.sort(reverse=True,key=lambda x:x[1])
f=0
#print(l) l=[i for i in range(4)]
for i in l:
    #print(t,i)
    if(t<=0):
        break
    elif(t<i[1]):
        f+=max([(j[0]-j[1]+t) for j in l if t<j[1]])
        break
    else:
        f+=i[0]
        t-=i[1]
print(f)
