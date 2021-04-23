#time limit error
for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input().strip()
    if(s.count("*")<k):
        print("NO")
        continue
    k='*'*k
    if k in s:
        print("YES")
    else:
        print("NO")
