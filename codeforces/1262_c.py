for _ in range(int(input())):
    n=int(input())
    s=1
    i=1
    if(n==1):
        print(1)
        continue
    while True:
        if n<=i:
            print(i)
            break
        elif n<=s:
            print(s)
            break
        i*=3
        s+=i
