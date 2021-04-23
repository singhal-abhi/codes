'''
1=20
2=36
3=51

4=44+4*4
'''
def f(n):
    if(n==1):
        return 20
    elif(n==2):
        return 36
    elif(n==3):
        return 51
    else:
        return 60
for _ in range(int(input())):
    n=int(input())
    if(n>4):
        if(n%4==0):
            s=44*n//4+16
        else:
            s=n//4*44+f(n%4)+4*(4-n%4)
    else:
        s=f(n)
    print(s)
