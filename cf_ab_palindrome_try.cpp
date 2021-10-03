#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    
    ll t;
    cin>>t;
    while(t--)
    {
        string s;
        int c0,c1,n;
        cin>>c0>>c1;
        cin>>s;
        ll i;int pre=0;
        for(i=0;i<s.size();i++)
        {
            if(s[i]=='0')
            {
                c0--;
                if(s[n-1-i]=='1')
                {
                    pre=-1;
                    break;
                }
                else if(s[n-1-i]=='?')
                {
                     s[n-1-i]='0';
                     c0--;
                }
                else
                {
                    c0--;
                }
                   
            }
            else if(s[i]=='1')
            {
                c1--;
                if(s[n-1-i]=='0')
                {
                    pre=-1;
                    break;
                }
                else if(s[n-1-i]=='?')
                {
                     s[n-1-i]='1';
                     c1--;
                }
                else
                {
                    c1--;
                }
            }
            else
            {
                if(s[n-1-i]=='?')
                {
                    if(c0>=c1)
                    {
                        s[i]='0';
                        s[n-1-i]='0';
                        c0=c0-2;
                    }
                    else
                    {
                        s[i]='1';
                        s[n-1-i]='1';
                        c1=c1-2;
                    }
                }
            }
        }
        if(pre==-1)
        {
            cout<<"-1\n";
        }
        else
        {
            cout<<s<<endl;
        }
    }
    return 0;
}
