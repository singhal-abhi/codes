#include<stdio.h>
main()
{
    //dout he
    int a,b,c;
    scanf("%d%d%d",&a,&b,&c);
    (b>a)?(b>c)?printf("b"):printf("c"):(a>c)?printf("a"):printf("c");
}
