for _ in range(int(input())):
    n=int(input())
    l=input().strip()
    p=l.count('1')
    if(120-n+p>=90):
        print("YES")
    else:
        print("NO")
