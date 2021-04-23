#include<bits/stdc++.h>
using namespace std;
int f2(int n)
{
    int c=0;
    while(n%2==0)
    {
        c++;
        n/=2;
    }
    return c;
}
int f3(int n)
{
    int c=0;
    while(n%3==0)
    {
        c++;
        n/=3;
    }
    return c;
}
main()
{
   int t;
   cin>>t;
   while(t--)
   {
       long long n;
       int c2,c3;
        cin>>n;
        if(n==1)
            {cout<<"0";
            continue;}
        for(int i=5;i<sqrt(n);i+=2)
            if(n%i==0)
        {
            cout<<-1;
            continue;
        }

        c2=f2(n);
        c3=f3(n);
           if(c2>c3||n%5==0)
            cout<<-1<<"\n";
           else
            cout<<c3+c3-c2<<"\n";

   }
}
