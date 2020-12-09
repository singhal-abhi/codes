#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int t,n,i;
    cin>>t;
    while(t--)
    {
        cin>>n;
        n=min(n,4);
        int a[n];
        for(i=0;i<n;i++)
            cin>>a[i];
        sort(a,a+n);

        switch(n)
        {
            case 1:cout<<a[0];break;
            case 2:cout<<max(a[0],a[1]);break;
            case 3:cout<<max((a[0]+a[1]),a[2]);break;
            case 4:if(a[3]>=(a[0]+a[1]+a[2]))
                        cout<<a[3];
                   else
                        cout<<max(a[0]+a[3],a[1]+a[2]);

        }
    }
}
