#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back
#define rep(i,a,b) for(int i=a;i<b;i++)
#define pii pair<int, int>
#define fr first
#define sc second
void solve(){
  int n; cin >> n;
  vector<int> a(n+1);
  rep(i, 1, n+1) cin >> a[i];
  sort(a.begin(), a.end());
  ll ans = 0;
  rep(i, 1, n+1){
    if(i == n){
      ans += (n-1) * 1LL * a[i];
    }
    else ans += i* 1LL *a[i];
  }
  rep(i, 1, n+1)
  ans += a[i];
  cout<<ans<<"\n";
}
signed main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);cout.tie(NULL);
  int t = 1;
  // cin >> t;
  while(t--){
    solve();
  }
  return 0;
}
