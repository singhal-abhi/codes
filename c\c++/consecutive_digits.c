#include<stdio.h>
#include<math.h>
main()
{
    int a,b,n,t,i,c=0,j;   //n for no of digits
    printf("enter range:");
    scanf("%d  %d",&a,&b);
    for(i=a;i<=b;i++)
    {
        t=i;
        for(n=0;t>0;t/=10,n++);
        t=i;
       /* for(;n>0;n--)
        {
            if(i%10!=i%100+1)
            {
                break;
            }
            i=i/10;
        }
        i=t;
        if(n==0)
            printf("%d ",i);*/
        int ar[n];

        for(j=0;j<n;j++)
        {
            ar[j]=t%10;
            t=t/10;

        }


        t=i;
        c=0;

        for(j=0;j<n-1;j++)
        {
           if(ar[j]-1!=ar[j+1])
           c=1;
        }

        if(c==0)
            printf("%d ",i);
    }
}
