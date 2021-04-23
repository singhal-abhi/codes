#include<stdio.h>
#include<math.h>
main()
{
    int t,n,w;
    int i,j;
    int pr;

     scanf("%d",&t);
    while(t>0)
    {
        pr=0;
        scanf("%d",&n);
        int p[n];

        for(i=0;i<n;i++)    //car price input
             scanf("%d",&p[i]);

        for(i=0;i<n-1;i++)
            for(j=0;j<n-i-1;j++)
            if(p[j]<p[j+1])
            {
                w=p[j];
                p[j]=p[j+1];
                p[j+1]=w;
            }

        for(i=0;i<n;i++)
           if(p[i]>0)
            pr=p[i]+pr-i;
        else continue;

        printf("%d",pr);
        t--;
    }

}
