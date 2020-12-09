#include<stdio.h>

main()
{
   int n,t,i,p,f,j,h;
   scanf("%d",&t);
   for(f=1;f<=t;f++)
   {
       scanf("%d%d",&n,&p);
       if(n>=p)
       {
           h=0;
           int s[n];
           for(i=0;i<n;i++)
           scanf("%d",&s[i]);
          /* for(i=0;i<n-1;i++)
            for(j=0;j<n-i-1;j++)
             if(s[j]>s[j+1])
             {
                 s[j]=s[j]+s[j+1];
                 s[j+1]=s[j]-s[j+1];
                 s[j]=s[j]-s[j+1];
             }*/
             for(i=0;i<p-1;i++)
             h+=(s[p-1]-s[i]);
             printf("Case #%d: %d",f,h);


       }
   }
}
