#include <iostream>
using namespace std;

int main()
{
int i, j, n, k = 0;
cin >> n;
for(i = 1; i <= n; i++)
{
for(j = i; j <= n; j++)
{
if (i == 1 || j == i || j == n)
cout << j;
else
cout << " ";
}
cout << endl;
}
return 0;
}
