#include <bits/stdc++.h>
using namespace std;
//write a program to calculate power 
int power(int m,int n)
{
    if(n==1)
    return 0;
    else return power(m,n-1)*(m+1);
}
int main()
{
    int r= power(2,3);
    cout<<"result is :"<<r;
    return 0;
}
