#include<stdio.h>
main()
{
    int i,j,k ;
    for(k=1;k<5;k++)
    {
        for(j=1;j<k;j++)
           {
               printf("%d",j);
           }
            for(i=k;i<5;i++)

                printf(" ");
             }
                printf("\n");
    }


