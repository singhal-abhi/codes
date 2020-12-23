for _ in range(int(input())):
    s=input()
    s=[int(i) for i in s]
    n=s[0]
    a=sum(s)
    if(a<9):
        print(str(a)+'9'*n)
    else:
        print(*s,sep="",end="")
        print('9'*s[0])
        
