#include<iostream>
using namespace std;
long f(long n)
{
    long i;
    for(i=2;i<n/2;i++)
        if(n%i==0)
        return i;
    return n;
}
int main()
{
    long n,k;
    int t;
    cin>>t;
    while(t--)
    {
        cin>>n>>k;
        for(;k>0;k--)
            n+=f(n);
        cout<<n;
    }
    return 0;
}
