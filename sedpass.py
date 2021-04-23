#wrong
import itertools
for _ in range(int(input())):
    s=input().strip()
    l=[]
    q=0
    for i in range(2,len(s),2):
        l+=itertools.combinations(s,i)
    for i in l:
        d={}
        for j in i:
            d[j]=d.get(j,0)+1
        c=0
        for j in d.values():
            if(j%2!=0):
                c+=1
                s=j
        if c==1 and (i.count('?')+j)%2==0:
            q+=1
    print(q)
