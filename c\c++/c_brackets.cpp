
#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back
#define rep(i,a,b) for(int i=a;i<b;i++)
#define pii pair<int, int>
#define fr first
#define sc second
int d(int n)
{
    for(int i=3;i<n/2;i+=2)
        if(n%i==0)
        return i;
    return 0;
}
void solve()
{
    int n,l;
    cin>>n;
    if(n==1)
        cout<<"FastestFinger";
    else if(n==2)
        cout<<"Ashishgup";
    else if(n&1)
        cout<<"Ashishgup";
    else{
        l=d(n);
        if(l==0||n/l==2)
            cout<<"FastestFinger";
        else
            cout<<"Ashishgup";
    }
}


signed main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);cout.tie(NULL);
  int t;
  cin >> t;
  while(t--){
    solve();
  }
  return 0;
}
