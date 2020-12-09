#include<stdio.h>
main()
{
 int x,i,max=0,t;
 scanf("%d",&x);
 int r[x],q[x];
 for(i=0;i<x;i++)
    scanf("%d",&r[i]);
 for(i=0;i<x;i++)
 {
    scanf("%d",&q[i]);
    t=q[i]/r[i];
    if(i==0)
        max=t;
    else if(max>t)
        max=t;
 }
 printf("%d",max);
}
