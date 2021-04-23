for _ in range(int(input())):
    s=int(input())
    n=0
    n+=int(s/100)
    s%=100
    n+=int(s/50)
    s%=50
    n+=int(s/10)
    s%=10
    n+=int(s/5)
    s%=5
    n+=int(s/2)
    s%=2
    n+=int(s)
    print(n)
