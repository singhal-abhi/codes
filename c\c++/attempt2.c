#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
     char *s[100],a[10]={0},i,j;
     scanf("%s",s);
    for(i=0;i<10;i++)
        for(j=0;*(s+j)!='\0';j++)
        if(i==*(s+j))
        a[i]++;

     for(i=0;i<10;i++)
     printf("%d ",a[i]);
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    return 0;
}
