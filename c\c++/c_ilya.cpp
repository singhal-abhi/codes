#include<iostream>
#include<stdio.h>
using namespace std;
main()
{
    int i,j,n,t;
    char s[100000];
    gets(s);
    cin>>t;
    while(t--)
    {
        cin>>i>>n;
        j=0;
        for(i=i-1;i<n-1;i++)
            if(s[i]==s[i+1])
            j++;
        cout<<j<<"\n";

    }
}
