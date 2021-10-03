#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	ll t;
	cin>>t;
	while(t--)
	{
	int n, k;
		cin >> n >> k;
		int c = 0;
		string ss;
		cin >> ss;
		int i = 0;
		while (ss[i] != '*')i++;
		ss[i] = 'x'; c++;
		// cout << i + k << endl;
		while (i + k < n) {
			int j = i + k;
			while (j > i and ss[j] != '*') { j--;}
			if (j == i)i += k;
			else {
				ss[j] = 'x';
				i = j;
				c++;
			}
		}
		i = n - 1;
		while (i >= 0 and (ss[i] != '*' and ss[i] != 'x'))i--;
		if (i >= 0) {
			if (ss[i] == '*')c++;
			ss[i] = 'x';
		}
		cout << c << endl;
	}
	return 0;
}
