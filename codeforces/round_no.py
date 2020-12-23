t=int(input())
while(t):
    t-=1
    n=list(input())
    c=len(n)
    for i in range(c):
        n[i]=int(n[i])*(10**(c-i-1))
    while True:
        try:
            n.remove(0)
        except:
            break
    print(len(n))
    print(*n)
