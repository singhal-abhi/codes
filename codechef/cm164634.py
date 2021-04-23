for _ in range(int(input())):
    n,x=map(int,input().split())
    s=set(map(int,input().split()))
    print(min(len(s),n-x))
