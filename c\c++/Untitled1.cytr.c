#include<stdio.h>
struct student
{
    char name[50];
    int roll;
    float age;
}s,*p;
main()
{
    p=&s;
    scanf("%s%d%f",&p->name,&p->roll,&p->age);
    printf("%s%d%f",p->name,p->roll,p->age);
}
