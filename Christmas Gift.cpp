#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    ll sc,i,n,min,c,ns,j,x;
    cin>>x;
    while(x--)
	{
	cin>>sc;
    for(i=0;i<sc;i++)
    {
       n=sc;
       min=99999;
       ns=sqrt(n);
       c=0;
       for(j=2;j<=ns;j++)
       {
           if( n % j == 0)
           {
               c++;
               break;
           }
       }
       if(c==0)
       min = n+2 ;
       else
       {
           for(j=1;j<=n/2;j++)
           {
               if(n%j == 0)
               for(ll k=1;k<=n/2;k++)
               {
                   if(n%k==0)
                   for(ll l=1;l<=n/2;l++)
                   {
                       if(j*k*l == n && (j+k+l <= min))
                       {
                            min=j+k+l;
                       }
                   }
               }
           }
       }
    }
    cout<<min<<"\n";
    }
    return 0;
}
