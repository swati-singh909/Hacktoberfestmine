#include<bits/stdc++.h>

using namespace std;

int main()
{      
	int cof1,cof2,cof3,cons;
	cout<<"enter coff for x^3 x^2 x and constans\n";
       //	cin>>cof1>>cof2>>cof3>>cons;
       //
       //	cout<<"\nenter value of x\n";
       //	cin>>x;
	cof1=1;cof2=0;cof3=-1;cons = -1;
	cout<<"y = "<<cof1<<"x^3 + "<<cof2<<"x^2 + "<<cof3<<"x + "<<cons;
	int n=0;
	float a,b,dp;
	cout<<"\n enter a and b and decimal places\n";
       //	cin>>a>>b>>dp;
       a=0;
       b=1;
       dp=1;
	n = (log10(b-a) + dp)/log10(2);
	n=n+1;
	cout<<n<<" "<<log10(2)<<"\n";
	for(int i=1;i<=n;i++)
	{
	      float x;
	      x = (a + b)/2;
	     // cout<<x;
	     //	float eq = (cof1*x*x*x) + (cof2*x*x) + (cof3*x) + (cons);// algebric
		float eq = x - cos(x); //trans...
		cout<<"x "<<i-1<<"is "<<x<<"  and value of y is "<<eq<<"\n";
		if (eq>0)
		b=x;
		else if(eq<0)
		a=x;
		else if(eq==0)
		{
		cout<<"sol is"<<x;break; }
		else
		cout<<"invalid";
	}

	return 0;
}
