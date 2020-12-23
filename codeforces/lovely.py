n=int(input())
def f(n):
    l=[n]
    for i in range(1,n//2+1):
        if(n%i==0):
            l.append(i)
    l[-1],l[0]=l[0],l[-1]
    return l
def l(n):
    for i in range(2,n//2):
        if(n%(i**2)==0):
            return False
    return True
s=sorted(f(n))
s.reverse()
for i in s:
    if(l(i)):
        print(i)
        exit()
