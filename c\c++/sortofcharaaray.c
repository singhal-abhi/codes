//sorting of names
#include<stdio.h>
#include<string.h>
main()
{
    int n,i,j;
    scanf("%d",&n);
    char s[n][100],w[100];
    for(i=0;i<n;i++)
        gets(s[i]);
    for(i=0;i<n;i++)
    {
        for(j=0;s[i][j]!='\0'&&i+1<n;j++)
            if(s[i][j]>s[i+1][j])
            {
                strcpy(w,s[i+1]);
                strcpy(s[i+1],s[i]);
                strcpy(s[i],w);
                i++;
            }

    }
    for(i=0;i<n;i++)
        printf("%s\n",s[i]);
}
