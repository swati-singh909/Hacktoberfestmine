#include <stdio.h>
#define MAX 10
int main()
{
	int a[MAX];
	int n,i,j,s,d,carry=0,sum;
	for(i=0;i<MAX;i++)
		a[i]=0;
	printf("enter no. of digits ");
	scanf("%d",&n);
	if(n>MAX)
	{
		printf("no. of digits exceeded the limit");
		printf("\nTerminating program....");
		return 1;
	}
	else
	{
		for(i=MAX-n,j=1;i<MAX;i++,j++)
		{
		    printf("enter %d digit ",j);
		    scanf("%d",&d);
		    //expected input 0-9
		    //if more than one digit is entered
		    //like 43 or 10089
		    //only last digit will be taken
			a[i]=d%10;
		}
		printf("no. you gave is ");
		for(i=MAX-n;i<MAX;i++)
		    printf("%d",a[i]);
		printf("\nenter a no. >=1 and <=9 to add ");
		scanf("%d",&s);
		for(i=MAX-1,j=0;i>=0;i--)
		{
			int temp=a[i];
			sum=a[i]+s%10+carry;
			a[i]=sum%10;
			carry=sum/10;
			s/=10;
			//counting the no. of digits change in the array
			if(a[i]!=temp)
			{
				j+=1;
			}
		}
		if(j>n&&j<MAX)
			n+=1;
		printf("Result : \n");
		for(i=MAX-n;i<MAX;i++)
			printf("%d",a[i]);
	}
	return 0;
}
