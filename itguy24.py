for _ in range(int(input())):
    n,k=map(int,input().split())
    c=0
    for i in range(1,n//2+1):
        j=n-i**k
        
