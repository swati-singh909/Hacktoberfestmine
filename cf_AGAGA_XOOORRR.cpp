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
       ll n;
       cin>>n;
       ll i,a[n],m,o;
       for(i=0;i<n;i++)
       {
           cin>>a[i];
       }
               ll k=a[0];
        for( i=1;i<n;i++)
            k=k^a[i];
            bool flag=0;
            if(flag)
            {
                cout<<"-1";
            }
        if(!k)
           { cout<<"YES\n";continue;}
       
         m=0;
        ll j,l=0;
        for(i=1;i<n;i++)
        {
            if(flag==1)
            {
                break;
            }
            m=0;l=0;
            for(j=0;j<i;j++)
            {
                m=m^a[j];
            }
            l=m^k;
            o=0;
            
            for(;j<n;j++)
            {
                o=o^a[j];
                ll x=l^o;
                if(m==x && o==x)
                {
                    flag=1;break;
                }
            }
        } 
        if(flag==0)
        {
            cout<<"NO\n";
        }
        else
        {
            cout<<"YES\n";
        }
        
   }
    return 0;
}
