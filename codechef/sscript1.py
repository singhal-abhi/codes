for _  in range(int(input())):
    n,k=map(int,input().split())
    s=input().strip()
    c='*'
    a=0
    for i in range(n):
        if(s[i]!=c):
            a=0
            continue
        a+=1
        if(a==k):
            break
    else:
        print("NO")
        continue
    print("YES")
