/*
*
* Hollow Edge Multiple of N Pattern 
*
* n = 5
*   5  10  15  20  25 
*  80              30 
*  75              35 
*  70              40 
*  65  60  55  50  45 
* 
* n = 7
*   7  14  21  28  35  42  49 
* 168                      56 
* 161                      63 
* 154                      70 
* 147                      77 
* 140                      84 
* 133 126 119 112 105  98  91 
* 
* n = 10
*  10  20  30  40  50  60  70  80  90 100 
* 360                                 110 
* 350                                 120 
* 340                                 130 
* 330                                 140 
* 320                                 150 
* 310                                 160 
* 300                                 170 
* 290                                 180 
* 280 270 260 250 240 230 220 210 200 190 
*
*/
#include <stdio.h>
int main()
{
	int n,i,j,k,l,m;
	scanf("%d ",&n);
	k=n*n;
	l=3*n*n-n;
	m=4*n*n-3*n;
	for(i=n;i<=n*n;i+=n)
	{
		for(j=n;j<=n*n;j+=n)
		{
			if(i==n)
				printf("%3d ",j);
			else if(j==n*n)
				printf("%3d ",k+=n);
			else if(i==n*n)
				printf("%3d ",l-=n);
			else if(j==n)
				printf("%3d ",m-=n);
			else
				printf("    ");
		}
		printf("\n");
	}
	return 0;
}
