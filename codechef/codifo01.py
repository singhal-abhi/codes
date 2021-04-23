for _ in range(int(input())):
    n,k=map(int,input().split())
    l=0
    try:
        if(k==1):
            l+=1
        if(bin(n)[k+1]=="1"):
            l+=1
        if(n%2==0 and k==1):
            l+=1
        for i in range(3,n//2+1,2):
            if(n%i==0):
                if(bin(i)[k+1]=="1"):
                    l+=1
    except:
        pass
    print(l)
