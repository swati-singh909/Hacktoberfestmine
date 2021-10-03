#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
void fastio()  {ios_base::sync_with_stdio(false); cin.tie(NULL); }
int main()
{
    fastio();
    ll t;
    cin>>t;
    while(t--)
    {
        ll n,k;
        cin>>n>>k;
        ll i,a[n];
        for(i=0;i<n;i++)
        {
            cin>>a[i];
        }
        i=0;ll x=n-1;
        while (i < n - 1 and k > 0) {
			while (a[i] == 0)i++;
			if (i == n)break;
			a[i]--;
			a[x]++;
			k--;
		}
        for(i=0;i<n;i++)
        {
            cout<<a[i]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
