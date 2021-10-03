#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    
    ll t;
    cin>>t;
    while(t--){
		int c0,c1;
		cin>>c0>>c1;
		string s;
		cin>>s;
		int n=s.length();
		bool pre=1;
		for(int i=0;i<n;i++){
			if(s[i]!='?'){
				if(s[n-i-1]!=s[i] and s[n-i-1]!='?')
				{
				pre=0;break;
				}
				if(s[n-i-1]=='?')
				{
				    s[n-i-1]=s[i];
				}
			}
		}
		
		for(int i=0;i<n;i++)
		if(s[i]=='0')
		c0--;
		else if(s[i]=='1') 
		c1--;
		
		for(int i=0;i<n;i++){
			if(s[i]=='?'){
				if(s[n-i-1]!='?')
				{pre=0;break;}
				if(c0>1)
				{s[i]='0';s[n-i-1]='0';c0-=2;}
				else if(c1>1)
				{s[i]='1';s[n-i-1]='1';c1-=2;}
				else if(i==n/2 and n&1){
					if(c0)
					{s[i]='0';c0--;}
					else 
					{s[i]='1';c1--;}
				}
			}
		}
		if(c0!=0 or c1!=0 or !pre)
		cout<<-1<<endl;
		else 
		cout<<s<<endl;

	}
    return 0;
}
