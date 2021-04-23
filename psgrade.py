for _ in range(int(input())):
    l=list(map(int,input().split()))
    if(sum(l[-3:])<l[-4]):
        print("NO")
    elif(l[0]>l[-3] or l[1]>l[-2] or l[2]>l[-1]):
        print("NO")
    else:
        print("YES")
