from sys import stdin,stdout
def get_l():
    return list(map(int,stdin.readline().strip().split()))
def printf(a,s=""):
    stdout.write(str(a)+str(s))
for _ in range(int(input())):
    n=int(input())
    s=input().strip()
    for i in range(0,n,4):
        a=int(s[i:i+4],2)
        print(chr(a+97),end="")
    print("\n")
