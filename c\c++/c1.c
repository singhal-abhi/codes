#include<stdio.h>

struct ts       //training set
{
    char w[5];
    int s;
};

char c=0;

void f(int t)
{
    int k,N,j=0,i;
    printf("enter N\n");
    scanf("%d",&N);

    struct ts a[t][N];

    k=0;
    for(;k<N;k++)
    {
       printf("enter ts\n");
       gets(a[t][k].w);
       scanf("%d",&a[t][k].s);
    }
    for(k=0;k<N;k++)
    {
        for(i=k+1;i<N;i++)
            if(strcmp(a[t][k].w,a[t][i].w)==0)
        {
            if(a[t][k].s==a[t][i].s)
                j=1;
            else
                j=0;
        }

    }c=c+j;
printf("%d\n",c);
}

main()
{
    int i,t;
    printf("enter no of test cases\n");
    scanf("%d",&t);
    for(i=0;i<t;i++)
        f(i);

}
