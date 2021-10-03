#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll SubStr(string X, string Y, ll m, ll n)
{
	ll LCSuff[m + 1][n + 1];
	ll result = 0,i,j; 
	for ( i = 0; i <= m; i++)
	{
		for (j = 0; j <= n; j++)
		{
			if (i == 0 || j == 0)
				LCSuff[i][j] = 0;

			else if (X[i - 1] == Y[j - 1]) {
				LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1;
				result = max(result, LCSuff[i][j]);
			}
			else
				LCSuff[i][j] = 0;
		}
	}
	return result;
}
int main()
{
	ll t;
	cin>>t;
	while(t--)
	{
		string sa, sb;
		cin >> sa >> sb;
		ll n = sa.size();
		ll m = sb.size();
		ll cm = SubStr(sa, sb, n, m);
		ll d=n + m - 2 * cm;
		cout << d << endl;
	}
	return 0;
}
