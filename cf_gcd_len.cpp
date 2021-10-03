#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll a,b,c;
        cin>>a>>b>>c;
        ll n1=pow(10,a-1),n2=pow(10,b-1);
        if(n1<n2)
        {
            n1=n1+pow(10,c-1);
        }
        else
        {
            n2=n2+pow(10,c-1);
        }
        cout<<n1<<" "<<n2<<endl;
    }
    return 0;
}
    
