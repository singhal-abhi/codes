#wa
for _ in range(int(input())):
    s=input().strip()
    if(len(s)%2!=0):
        print(-1)
        continue
    print(abs(n//2-s.count('1')))
