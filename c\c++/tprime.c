#include<stdio.h>
main()
{
    long int i,j,n,c;
    scanf("%ld",&n);
    long long int a[n];
    for(i=0;i<n;i++)
        scanf("%I64d",&a[i]);
    for(i=0;i<n;i++)
    {
        c=0;
        for(j=2;j<a[i]/2+1&&j<66666;j++)
        {
            if(a[i]%j==0)
            c++;
            if(c>1)
                break;
        }
        if(c==1)
            printf("YES\n");
        else
            printf("NO\n");
    }
}
