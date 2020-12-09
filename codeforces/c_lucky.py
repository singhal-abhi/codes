s=input()
d={}
d[7]=0
d[4]=0
for i in s:
    if(i=='4'or i =='7'):
        i=int(i)
        d[i]=d.get(i,0)+1
if(d[7]==0 and d[4]==0):
    print(-1)
    exit()
if(d[7]>d[4]):
    print(7)
else:
    print(4)
