for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=0
    i=0
    while(i<n):
        if(l[i]==1):
            j=i
            while(j<n-1 and l[j+1]-l[j]==1):
                j+=1
            if abs(j-i)>m:
                m=j-i+1
            i=j
        i+=1
    print(m)
