#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll n,k;
        cin>>n>>k;
        ll i,a[n]={};
        
        if(k>(n-1)/2)
        {
            cout<<"-1\n";
        }
        else
        {
            i=1;
            ll x=n;
            while(k--)
            {
                a[i]=x;
                x--;
                i=i+2;
            }
            x=1;
            for(i=0;i<n;i++)
            {
                if(a[i]==0)
                {
                    a[i]=x;
                    x++;
                }
                cout<<a[i]<<" ";
            }
            cout<<endl;
        }
        
    }
    return 0;
}
