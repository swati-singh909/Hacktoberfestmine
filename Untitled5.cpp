#include<iostream>
using namespace std;
int main()
{
	int n;
	cin>>n;
	int maxCandy;
	cin>>maxCandy;
	int home[n];
	for(int h=0;h<n;h++)
	{
		cin>>home[h];
	}
	int i, j;
	int grandSum=0, s, l;
	int sum=0;
	
	int count=0;
	for(int h=0;h<n;h++)
	{ 
	
	
		if(home[h]>maxCandy)
		{
			count++;
			
		}
	
		if(count==n)
		{
			cout<<"NO CANDIES";
			return 0;
		}
	}
	
	for(int i=0;i<n;i++)
	{
		sum=0;
		j=i;
		while(sum<maxCandy && j<n)
		{
			sum=sum+home[j];
			j++;
			
			
		}
		
		if(sum>20)
		{

			sum=sum-home[--j];

		}
		
		
		if(sum>grandSum)
		{
			grandSum=sum;
			s=i;
			l=j;
		}
		
	}

	cout<<"First Home: "<<s+1<<endl;
	cout<<"Last Home: "<<l<<endl;
	cout<<"Total Candies: "<<grandSum<<endl;
	
	
	
	
	
	
	return 0;

}
