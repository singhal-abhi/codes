#include<stdio.h>
void main()
{
int m ,n,i,j,c;
printf("enter size of set a and b");
scanf("%d%d",&m,&n);
int a[m],b[n];
for(i=0;i<m;i++)
    scanf("%d",&a[i]);
for(i=0;i<n;i++)
    scanf("%d",&b[i]);
printf("enter 1 for a-b and 2 for b-a");
scanf("%d",&c);
if(c==1)
{
    for(i=0;i<n;i++)
        for(j=0;j<m;j++)
        if(b[i]==a[j])
        a[j]=NULL;
    for(i=0;i<m;i++)
        if(a[i]!=NULL)
        printf("%d\t",a[i]);
}
else if (c==2)
{
    for(i=0;i<m;i++)
        for(j=0;j<n;j++)
        if(b[i]==a[j])
        b[j]=NULL;
    for(i=0;i<n;i++)
        if(b[i]!=NULL)
        printf("%d\t",b[i]);
}
}
