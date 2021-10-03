#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    
    ll t;
    cin>>t;
    while(t--)
    {
        ll i,j,n;
        cin>>n;
        char a[n][n];
        bool b=0;
        ll x1,x2,y1,y2;
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                cin>>a[i][j];
                if(a[i][j]=='*')
                {
                    if(!b)
                    {
                        x1=i;
                        y1=j;
                        b=1;
                    }
                    else
                    {
                        x2=i;
                        y2=j;
                    }
                }
            }
        }
        // cout<<"x1="<<x1<<" x2 = "<<x2<<" \ny1 ="<<y1<<" y2= "<<y2<<endl;
        if(x1!=x2 && y1!=y2)
        {
            a[x1][y2]='*';
            a[x2][y1]='*';
        }
        else if(x1==x2)
        {
            if(x1+1<n)
            {a[x1+1][y1]='*';
            a[x2+1][y2]='*';
            }
            else
            {
                a[x1-1][y1]='*';
            a[x2-1][y2]='*';
            }
        }
        else
        {
            if(y1+1<n)
            {
                a[x1][y1+1]='*';
            a[x2][y2+1]='*';
            }
            else
            {
                a[x1][y1-1]='*';
            a[x2][y2-1]='*';
            }
        }
        
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                cout<<a[i][j];
            }
            cout<<endl;
        }
    }
    return 0;
}
