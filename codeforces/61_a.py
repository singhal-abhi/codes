s=input()
t=input()
x=""
for i in range(len(s)):
    x+=str(int(s[i])^int(t[i]))
print(x)
