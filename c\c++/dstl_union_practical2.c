#include<stdio.h>
main()
{
    int n,i,t;
    printf("enter size of array 1\n");
    scanf("%d",&n);
    int a[n];
    printf("Enter array 1\n");
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    printf("enter size of array 2\n");
    scanf("%d",&t);
    printf("enter array 2\n");
    int b[t+n];
    for(i=0;i<t;i++)
    scanf("%d",&b[i]);
    int j=i,c,k;
    for(i=0;i<n;i++)
    {
        c=0;
        for(k=0;k<t;k++)
            if(a[i]==b[k])
                c=1;
        if(c==0)
        {
            b[j]=a[i];
            j++;
        }

    }
    for(i=0;i<j;i++)
        printf("%d\t",b[i]);

}
