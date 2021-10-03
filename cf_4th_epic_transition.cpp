#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	ll t;
	cin>>t;
	while(t--)
	{
	ll n;
		cin >> n;
		ll a[n];
		unordered_map<ll,ll>mpa;
		set<ll>s;
		ll i=0;
		while(i<n)
		{
		    cin >> a[i];
		mpa[a[i]]++;
		s.insert(a[i]);
		i++;
		}

		vector<ll>p;
		for (auto i : mpa) {
			p.push_back(i.second);
		}
		sort(p.begin(), p.end(), greater<int>());
		if (s.size() > ((n + 1) / 2)) {
			if (n & 1)cout << 1 << endl;
			else cout << 0 << endl;
		}
		else {
			if (p[0] > (n + 1) / 2)cout << 2 * p[0] - n << endl;
			else {
				if (n & 1)cout << 1 << endl;
				else cout << 0 << endl;
			}
		}

	}
	return 0;
}
