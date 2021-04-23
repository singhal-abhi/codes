for _ in range(int(input())):
    s=input()
    c=0
    while True:
        x=s
        t=bin(c)[2:]
        for i in t:
            if i in x:
                x=x[x.index(i)+1:]
            else:
                break
        else:
            c+=1
            continue
        print(t)
        break
