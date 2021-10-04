
#include <bits/stdc++.h>

using namespace std;



int main ()
{
	string str;
	cout<<"Enter the string...\n";
	cin>>str;
	int count=0;
	
	for(int i=0;i<str.size();i++)
	{
		if(str[i]=='a' || str[i]=='A' || str[i]=='e' || str[i]=='E' || str[i]=='i' || str[i]=='I' || str[i]=='o'|| str[i]=='O' || str[i]=='u' || str[i]=='U' )
		{
			count++;	
		}
	}
	cout<<"Number of vowels: "<<count;

	return 0;
}

