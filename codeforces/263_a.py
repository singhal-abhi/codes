l=[]
for i in range(5):
    l.append(list(map(int,input().split())))
for i in range(5):
    if(1 in l[i]):
        j=l[i].index(1)
        break
print(abs(2-i)+abs(2-j))
