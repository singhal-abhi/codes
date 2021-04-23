from sys import stdin,stdout
def get_l():
    return list(map(int,stdin.readline().strip().split()))
def printf(a,s="\n"):
    stdout.write(str(a)+str(s))
for _ in range(int(input())):
    n,k,d=map(int,input().split())
    l=get_l()
    n=min(sum(l)//k,d)
    printf(n)
