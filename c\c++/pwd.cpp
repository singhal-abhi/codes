#include<bits/stdc++.h>
using namespace std;
main()
{
    char s[100],q[100];
    cin>>s;
    int n,i,j=0;
    cin>>n;
    char l[n][100];
    for(i=0;i<n;i++)
    {
        cin>>q;
        if(s[0]==q[0])
        {
            l[j]=q;
            j++;
        }
    }


}
