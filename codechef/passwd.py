for _ in range(int(input())):
    s=input()
    if(len(s)<10):
        print("NO")
        continue
    if(any(x.isupper() for x in s[1:-1]) and any(x.islower() for x in s) and any(x.isdigit() for x in s[1:-1])):
        if(any(x in ['@', '#', '%', '&', '?' ] for x in s[1:-1])):
            print("YES")
            continue
    print("NO")
