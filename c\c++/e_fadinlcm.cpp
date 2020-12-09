#include<iostream>
using namespace std;
main()
{
    int i,j,n,c=10000,d=10000;
    cin>>n;
    if(n==4)
        cout<<"1 4";
    for(i=1;i<=n;i++)
        for(j=i;j<=n;j++)
        if(i*j==n)
        {
            if(max(i,j)<max(c,d))
            {
                c=i;
                d=j;
            }
        }
    cout<<c<<" "<<d;
}


