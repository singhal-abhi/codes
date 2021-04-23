
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void main()
{ int p, d,c,e,f,j;
  scanf("%d",&d);
      e=d;
     for(j=1;j<d;++j)
     {


         for(p=2;p<e;++p)
             {
             if(e%p==0)
             {

              f=0;
              break;
             }
         else
         {
                       f=1;

         }
  }
  if(f==1)
   {
       printf("%d\t",e);

   }
   e=e-1;  } }

