t=int(input())
def count(a):
    if a==0 or a==6 or a==9:
        return 6
    elif a==1:
        return 2
    elif a==2 or a==3 or a==5:
        return 5
    elif a==4:
        return 4
    elif a==7:
        return 3
    elif a==8:
        return 7
while t:
    t-=1
    a,b=map(int,input().split())
    a=a+b
    b=0
    while(a>0):
        b+=count(int(a%10))
        a=a//10
    print(b)
