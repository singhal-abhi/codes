#include<iostream>
using namespace std;
main()
{
    int n;
    cin>>n;
    long long a,e ,b;
    while(n--)
    {
        cin>>a>>b;
        e=a*(b-1)+b*(a-1);
        if(e<=a*b)
            cout<<"YES\n";
        else
            cout<<"NO\n";
    }
}
