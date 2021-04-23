#include<stdio.h>
void fun(){
    for(int i=1;i<(1<<2);i++){
        for(int j=0;j<2;j++)
            if((1<<j)&i)
                printf("%d ",i);
        printf("  ");
    }
}
main()
{
     int a = 1005,i,j;
    int b = 1050;
    int c = 0;
    for(i=1000,j=1000;j<b,i<a;i++,j++)
        c++;
    printf("%d",c);
    fun(5,2);
}
