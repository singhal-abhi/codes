for i in range(int(input())):
    l=input()
    l=list(map(int,input().split()))
    s=set(l)
    print(len(l)-len(s))
