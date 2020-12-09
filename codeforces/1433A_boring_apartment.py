t=int(input())
while(t):
    l=input()
    s=sum([i for i in range(1,len(l)+1)])
    l=int(l)
    s+=((l-1)%10)*10
    print(s)
    t-=1
