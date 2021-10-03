#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	ll t;
	cin>>t;
	while(t--)
	{
		ll n,m,x;
		cin>>n>>m>>x;
		x--;
		ll a,b;
		a=(x/n);
		b=x%n;
		b=b*m;
		a++;
		cout<<a+b<<endl;
	}
	return 0;
}
