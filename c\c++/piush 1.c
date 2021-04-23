#include<stdio.h>
main()
{int a,b,c,n;
printf("enter the no");
scanf("%d",&n);
a=n%10;
n=n/10;
b=n%10;
n=n/10;
c=a*100+b*10+n;
printf("%d is the reverse no",c);
}
