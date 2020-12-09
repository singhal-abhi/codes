t=int(input())
while(t):
    t-=1
    s=input().strip()
    if(len(s)>10):
        s=s[0]+str(len(s)-2)+s[-1]
    print(s)
