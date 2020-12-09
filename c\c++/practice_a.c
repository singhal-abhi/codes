#include<stdio.h>
main()
{
  int x,dh,dm,h,m;
  float y,z;
  scanf("%d%f",&x,&y) ;
  z=(x/360.0)*y;
  h=(int)z;
  m=(int)(z*100);
  m=(m%100)*60/100;

  dh=h*30+m*0.5;
  dm=m*6;
  if(dm>dh)
    x=dm-dh;
  else x=dh-dm;
  if(x==360)
    x=0;
  printf("%d",x);
}
